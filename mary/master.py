from ._formatter import get_master_help
from ._io import output
from ._messages import DescriptionMsg, ErrorMsg
from .base import Base

_GLOBAL_OPTIONS = {
    "version": "Display this application version",
    "help": "Display this help message",
}


class Master(Base):
    """Global CLI configuration."""

    cover = None  # TODO: print something nice

    app_name = "Mary"
    version = "0.1.0"
    options = None  # custom user options

    def __init__(self):
        self._command = self.parse.get_command()
        self._commands = {}

        self.parsed_options = self.parse.get_options(_GLOBAL_OPTIONS)
        if self.options:  # custom user options for Master
            self.options = self.parse.get_options(self.options)

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

        # TODO: fix his hardcoded crap
        for option in self.parsed_options:
            if option.short_flag == self._command or option.long_flag == self._command:
                if option.short_flag == "-h" or option.short_flag == "--help":
                    output(self._main_help())
                    break
                elif option.short_flag == "-v" or option.long_flag == "--version":
                    output(f"{self.app_name} {self.version}")
                    break
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
