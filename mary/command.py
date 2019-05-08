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
        self._run()

    def _command_help(self):
        """
        Generate the help message.
        """
        description = self._get_doc()
        if description is None:
            description = DescriptionMsg.no_description(self.command_name)

        help_msg = get_command_help(description, self.argument, self.command_name)
        print(help_msg)

    def _get_doc(cls):
        if cls.__doc__:
            return cls.__doc__.strip()

    def handler(self):
        """
        The handler of the command.
        """
        pass

    def _run(self):
        if self.argv_argument:
            self.argument = self.argv_argument
            return self.handler()

        return self._command_help()
