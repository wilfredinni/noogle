from ._formatter import get_command_help
from ._messages import DescriptionMsg
from .base import Base


class Command(Base):
    """
    Base class for implementing commands
    """

    command_name = None  # str: caller of the command
    argument = None  # dict: {name: help} provided by the developer
    options = None  # dict: {name: help}

    def __init__(self):
        self.argv_argument = self.parse.get_argument()  # Terminal argvs
        self._run()

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
        print(help_msg)

    def handler(self):
        """
        The handler of the command.
        """
        raise NotImplementedError()

    def _run(self):
        if self.argv_argument:
            self.argument = self.argv_argument
            return self.handler()

        return self._command_help()
