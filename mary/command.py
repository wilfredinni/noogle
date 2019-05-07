import sys

from ._messages import DescriptionMsg
from ._parser import _parse_command_help


class Command:
    """
    Base class for implementing commands
    """

    argument = None
    command_name = None

    def __init__(self):
        self.argument = self.get_argument()

        if self.argument:
            self.handler()

    def command_help(cls):
        """
        Generate the help message.
        """
        if cls.__doc__:
            description = cls.__doc__.strip()
        else:
            description = DescriptionMsg.no_description(cls.command_name)

        help_msg = _parse_command_help(description, cls.argument, cls.command_name)
        print(help_msg)

    def get_argument(self):
        try:
            return sys.argv[2]
        except IndexError:
            self.command_help()

    def handler(self):
        """
        The handler of the command.
        """
        pass
