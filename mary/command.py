import sys

from .parser import _parse_command_help


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
            help_msg = _parse_command_help(cls.__doc__, cls.argument, cls.command_name)
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
