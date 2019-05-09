from ._formatter import get_command_help
from ._io import output
from ._messages import DescriptionMsg
from .base import Base


class Command(Base):
    """Base class for implementing Commands."""

    command_name = None  # str: caller of the command
    argument = None  # dict: {name: help} provided by the users
    options = None  # dict: {name: help} provided by the user

    def __init__(self):
        self.argv_argument = self.parse.get_argument()  # Terminal argvs
        self.options = self.parse.get_options(self.options)
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
        If an argument is provided, the dict in self.argument(defined by
        the user) is override with the argument (sys.argv) to be used on
        the handler() method. Else, generate and print the help.
        """
        if self.argv_argument:
            self.argument = self.argv_argument
            return self.handler()

        return self._command_help()
