from ._messages import DescriptionMsg
from ._formatter import get_command_help
from ._parser import Parser


class Command:
    """
    Base class for implementing commands
    """

    argument = None
    command_name = None
    options = None

    def __init__(self):
        self.argv_argument = Parser.parse("argument")

        if self.argv_argument:
            self.argument = self.argv_argument
            self.handler()
        else:
            self.command_help()

    def command_help(cls):
        """
        Generate the help message.
        """
        if cls.__doc__:
            description = cls.__doc__.strip()
        else:
            description = DescriptionMsg.no_description(cls.command_name)

        help_msg = get_command_help(description, cls.argument, cls.command_name)
        print(help_msg)

    def handler(self):
        """
        The handler of the command.
        """
        pass
