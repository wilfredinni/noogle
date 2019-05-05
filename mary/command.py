import sys

from .parser import _parse_command_help


class Command:
    """
    Base class for implementing commands
    """

    help = None
    argument = None

    def __init__(self):
        self.description = self.command_description()
        self.argument = self.get_argument()

        if self.argument:
            self.handler()

    def command_description(cls):
        """
        Generate the help message.
        """
        if cls.__doc__:
            return _parse_command_help(cls.__doc__, cls.argument, cls.help)

    def get_argument(self):
        try:
            return sys.argv[2]
        except IndexError:
            self.cli_doc()

    def handler(self):
        """
        The handler of the command.
        """
        pass

    def cli_doc(self):
        """
        Generate the Info message for the CLI app.
        """
        if self.description:
            print(self.description)
