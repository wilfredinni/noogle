import os
import sys

from ._help_formatter import get_command_help, get_master_help
from ._messages import CliMsg, DescriptionMsg, ErrorMsg
from ._globals import (
    _GLOBAL_OPTIONS,
    _GLOBAL_COMMAND_OPTIONS,
    _HELP_FLAGS,
    _VERSION_FLAGS,
)
from ._parser import Parser
from .io import output


parse = Parser()


class Base:
    """
    Base class for both, Master and Command
    """

    def __init__(self, user_passed_options):
        # options passed on the command line
        self.user_passed_options = parse.get_options

    def _get_doc(self):
        if self.__doc__:
            return f"{self.__doc__.strip()}{os.linesep}"


class Master(Base):
    """
    Global CLI configuration.
    """

    app_name = None
    options = None
    version = "0.1.0"

    def __init__(self, user_passed_options=None):
        # passed options
        super().__init__(user_passed_options)
        self.passed_command = parse.get_command

        # all the registered commands (from self.register())
        self._commands = {}

        # common options like --help or --version
        self.default_options = parse.parse_options(_GLOBAL_OPTIONS)

        # if app_name is None, get the name of the script
        if not self.app_name:
            self.app_name = parse.get_app_name

    def _main_help(self):
        """
        Generate the Info message for the CLI app.
        """
        description = self._get_doc()
        if description is None:
            description = DescriptionMsg.no_description()

        return get_master_help(
            description, self._commands, self.default_options, self.options
        )

    def _execute_command(self):
        """
        Execute a registered Command.
        """
        if self.passed_command in self._commands.keys():
            return self._commands[self.passed_command]()

        output(ErrorMsg.wrong_command(self.passed_command))

    def _execute_flag(self):
        """
        Execute a Flag (default or user defined)
        """
        if self.user_passed_options[0] in _HELP_FLAGS:
            output(self._main_help())

        elif self.user_passed_options[0] in _VERSION_FLAGS:
            output(CliMsg.version(self.app_name, self.version))

        else:
            output(ErrorMsg.wrong_option(self.user_passed_options[0]))

    def register(self, *args):
        """
        Register a group of commands.
        """
        [self._commands.setdefault(command.command_name, command) for command in args]

    def run(self):
        """
        Execute the Command Line Interface.
        """
        if self.passed_command:
            return self._execute_command()

        elif self.user_passed_options:
            return self._execute_flag()

        output(self._main_help())


class Command(Base):
    """
    Base class for implementing Commands.
    """

    command_name = None  # str: caller of the command
    argument = None  # dict: {name: help} user defined
    options = {}  # dict: {name: help} user defined

    def __init__(self, user_passed_options=None):
        # passed options
        super().__init__(user_passed_options)

        # user-defined options
        self.user_options = parse.parse_options(self.command_options())

        # arguments passed on the command line
        self.passed_arguments = parse.get_argument

        # options shared by all the commands
        self.default_options = parse.parse_options(_GLOBAL_COMMAND_OPTIONS)

        self._run()

    def _command_help(self):
        """
        Generate the help message.
        """
        description = self._get_doc()
        if description is None:
            description = DescriptionMsg.no_description(self.command_name)

        help_msg = get_command_help(
            description,
            self.argument,
            self.command_name,
            self.default_options,
            self.user_options,
        )
        output(help_msg)
        sys.exit()

    def _check_options(self):
        if self.user_passed_options[0] in _HELP_FLAGS:
            self._command_help()

        # if the option is found (short or long flag), return to _run()
        if self.user_options:
            for opt in self.user_options:
                if opt.short_flag in self.user_passed_options:
                    return
                if opt.long_flag in self.user_passed_options:
                    return

        # else, output an OptionNotFound warning and exit the program
        output(ErrorMsg.wrong_option(self.user_passed_options[0]))
        sys.exit()

    def option(self, option):
        """
        Return True/False if the option valid. To be used with self.handler():
        """
        # user-defined options are in self.user_options and passed option in
        # self.user_passed_options. Option can be short (self.user_options[0].short_flag)
        # or long (self.user_options[0].long_flag)
        for opt in self.user_options:
            if opt.name == option:
                if opt.short_flag in self.user_passed_options:
                    return True
                elif opt.long_flag in self.user_passed_options:
                    return True
        return False

    def command_options(self):
        """
        Override this function with the command options. I.e:
        self.options["yell"] = "Yell in uppercase letters"
        """
        return self.options

    def handler(self):
        """
        The handler of the command.
        """
        raise NotImplementedError()

    def _run(self):
        """
        If an argument is provided, the dict in `self.argument` (defined
        by the user) is override with the argument (sys.argv) to be used on
        the `handler()` method. Else, generate and print the help.
        """
        # check for passed options. If invalid, output an OptionNotFound warning
        if self.user_passed_options:
            self._check_options()

        # check if an argument is needed to execute a command, and
        # if not, and one is passed anyway, output an ArgumentNeeded warning
        if self.argument and not self.passed_arguments:
            argument_name = [k for k in self.argument.keys()]
            output(ErrorMsg.no_argument(argument_name[0]))
            return

        # if the command don't need arguments, but one is passed anyway
        # output a TooManyArguments warning
        if self.passed_arguments and not self.argument:
            output(ErrorMsg.too_many_arguments(self.command_name))
            return

        # if the command don't need arguments to execute
        if not self.argument:
            return self.handler()

        if self.passed_arguments:
            # `self.passed_arguments` return a list of arguments. For now, to
            # retrieve the argument, I hardcoded to the first element of
            # the list. This wont work if the user need a a list of arguments.
            # Maybe a method on parse.get_argument (_parser.py).
            self.argument = self.passed_arguments[0]
            return self.handler()

        return self._command_help()
