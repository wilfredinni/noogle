from ._parser import Parser
from ._formatter import get_master_help
from ._io import output
from ._messages import DescriptionMsg, ErrorMsg, CliMsg
from ._formatter import get_command_help


_GLOBAL_OPTIONS = {
    "version": "Display this application version",
    "help": "Display this help message",
}

parse = Parser()


class Base:
    def _get_doc(cls):
        if cls.__doc__:
            return cls.__doc__.strip()


class Master(Base):
    """Global CLI configuration."""

    cover = None  # TODO: print something nice

    app_name = None
    version = "0.1.0"
    options = None  # custom user options

    def __init__(self):
        self._command = parse.get_command
        self._commands = {}

        if not self.app_name:
            self.app_name = parse.get_app_name

        # default and custom options
        self.parsed_options = parse.parse_options(_GLOBAL_OPTIONS)
        if self.options:  # custom user options for Master
            self.options = parse.parse_options(self.options)

    def _main_help(self):
        """Generate the Info message for the CLI app."""
        description = self._get_doc()
        if description is None:
            description = DescriptionMsg.no_description()

        return get_master_help(
            description, self._commands, self.parsed_options, self.options
        )

    def _execute(self):
        """Execute a Command or Flag (default or user defined)."""
        if self._command in self._commands.keys():
            return self._commands[self._command]()

        # TODO fix: undefined flag after a command prints help
        # HINT: this is because before the check for the flag the command is
        # executed (first if statement in this method). To output the expected
        # error message, create a check for flags inside the Command class.
        flags = parse.get_flags
        # print(flags)
        if "-h" in flags or "--help" in flags:
            output(self._main_help())

        if "-v" in flags or "--version" in flags:
            output(CliMsg.version(self.app_name, self.version))

        else:
            output(ErrorMsg.wrong_command(self._command))

    def register(self, *args):
        """
        Register all the commands.

        Arguments:
            *args {class} -- Classes that inherit from Command
        """
        [self._commands.setdefault(command.command_name, command) for command in args]

    def run(self):
        """Execute the Command Line Interface."""
        if self._command:
            return self._execute()

        output(self._main_help())


class Command(Base):
    """Base class for implementing Commands."""

    command_name = None  # str: caller of the command
    argument = None  # dict: {name: help} provided by the users
    options = None  # dict: {name: help} provided by the user

    def __init__(self):
        self.argv_argument = parse.get_argument  # Terminal argvs
        self.flags = parse.get_flags

        if self.options:
            self.options = parse.parse_options(self.options)

        self._run()

    def _command_help(self):
        """Generate the help message."""
        description = self._get_doc()
        if description is None:
            description = DescriptionMsg.no_description(self.command_name)

        help_msg = get_command_help(
            description, self.argument, self.command_name, self.options
        )
        output(help_msg)

    def handler(self):
        """The handler of the command."""
        raise NotImplementedError()

    def _run(self):
        """
        If an argument is provided, the dict in `self.argument` (defined
        by the user) is override with the argument (sys.argv) to be used on
        the `handler()` method. Else, generate and print the help.
        """
        # print(self.argv_argument)
        # TODO use len to turn self.argument to None if self.argv_argument is
        # an empty list. May be usefull letter on.
        if self.argv_argument:
            # `self.argv_argument` return a list of arguments. For now, to
            # retrieve the argument, is hardcoded to the first element of
            # the list. This wont work if the user need a a list of arguments.
            # Maybe a method on parse.get_argument (_parser.py).
            self.argument = self.argv_argument[0]
            print(self.argument)
            return self.handler()

        return self._command_help()
