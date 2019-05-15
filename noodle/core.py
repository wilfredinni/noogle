import sys

from ._formatter import get_command_help, get_master_help
from ._messages import CliMsg, DescriptionMsg, ErrorMsg
from ._parser import Parser
from .io import output

# import pysnooper


_GLOBAL_OPTIONS = {
    "version": "Display this application version",
    "help": "Display this help message",
}

parse = Parser()


class Base:
    """
    Base class for both, Master and Command
    """

    def _get_doc(self):
        if self.__doc__:
            return self.__doc__.strip()


class Master(Base):
    """
    Global CLI configuration.
    """

    cover = None  # TODO: print something nice cover
    app_name = None
    options = None
    version = "0.1.0"

    def __init__(self):
        self._commands = {}
        self.flags = parse.get_flags
        self.current_command = parse.get_command
        self.default_options = parse.parse_options(_GLOBAL_OPTIONS)

        if self.options:
            self.options = parse.parse_options(self.options)

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
        if self.current_command in self._commands.keys():
            return self._commands[self.current_command]()

        output(ErrorMsg.wrong_command(self.current_command))

    def _execute_flag(self):
        """
        Execute a Flag (default or user defined)
        """
        if "-h" in self.flags or "--help" in self.flags:
            output(self._main_help())

        elif "-v" in self.flags or "--version" in self.flags:
            output(CliMsg.version(self.app_name, self.version))

        else:
            # TODO: this shit is hardcoded and will bring doom if I don't fix it.
            output(ErrorMsg.wrong_command(self.flags[0]))

    def register(self, *args):
        """
        Register a command.
        """
        [self._commands.setdefault(command.command_name, command) for command in args]

    def run(self):
        """
        Execute the Command Line Interface.
        """
        if self.current_command:
            return self._execute_command()

        elif self.flags:
            return self._execute_flag()

        output(self._main_help())


class Command(Base):
    """
    Base class for implementing Commands.
    """

    command_name = None  # str: caller of the command
    argument = None  # dict: {name: help} provided by the user
    options = None  # dict: {name: help} provided by the user

    def __init__(self):
        self.passed_arguments = parse.get_argument  # Terminal argvs
        self.flags = parse.get_flags
        self.options = self._command_options
        self._run()

    @property
    def _command_options(self):
        if self.options:
            return parse.parse_options(self.options)

    def _command_help(self):
        """
        Generate the help message.
        """
        description = self._get_doc()
        if description is None:
            description = DescriptionMsg.no_description(self.command_name)

        help_msg = get_command_help(
            description, self.argument, self.command_name, self.options
        )
        output(help_msg)

    def handler(self):
        """
        The handler of the command.
        """
        raise NotImplementedError()

    def option(self, option):
        """
        Return True/False if the option valid.
        """
        # self.check_option(option)
        # user defined options are in self.options
        # current flag is in self.flags
        # option can be:
        # - short, -y (self.options[0].short_flag)
        # - long --yell (self.options[0].long_flag)
        for opt in self.options:
            if opt.name == option:
                if opt.short_flag in self.flags or opt.long_flag in self.flags:
                    return True

        return False

    def check_option(self):
        for opt in self.options:
            if opt.short_flag in self.flags or opt.long_flag in self.flags:
                return

        output(ErrorMsg.wrong_option(self.flags))
        sys.exit()

    def _run(self):
        """
        If an argument is provided, the dict in `self.argument` (defined
        by the user) is override with the argument (sys.argv) to be used on
        the `handler()` method. Else, generate and print the help.
        """
        # if an undefined flag is passed but no arguments
        if self.flags and not self.passed_arguments:
            self.check_option()

        # if a wrong flag is passed with an argument
        if self.flags and self.passed_arguments:
            self.check_option()

        # if there are user arguments defined, and a flag but arguments passed
        if self.argument and self.flags and not self.passed_arguments:
            argument_name = [k for k in self.argument.keys()]
            output(ErrorMsg.no_argument(argument_name[0]))
            sys.exit()

        if self.passed_arguments:
            # `self.passed_arguments` return a list of arguments. For now, to
            # retrieve the argument, is hardcoded to the first element of
            # the list. This wont work if the user need a a list of arguments.
            # Maybe a method on parse.get_argument (_parser.py).
            self.argument = self.passed_arguments[0]
            return self.handler()

        return self._command_help()
