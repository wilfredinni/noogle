import sys

from ._messages import ErrorMsg, DescriptionMsg
from ._parser import _parse_cli_description


class Master:
    """
    Global CLI configuration
    """

    def __init__(self):
        self.command = self._get_command()
        self.commands = {}

    def _main_help(cls, commands):
        """
        Generate the Info message for the CLI app.
        """
        if cls.__doc__:
            description = cls.__doc__.strip()
        else:
            description = DescriptionMsg.no_description()

        return _parse_cli_description(description, commands)

    def _get_command(self):
        try:
            return sys.argv[1]
        except IndexError:
            pass

    def _execute_command(self, command):
        if command in self.commands.keys():
            return self.commands[command]()

        print(ErrorMsg.wrong_command(command))

    def register(self, commands: list):
        """
        Register all the commands.
        """
        for command in commands:
            self.commands[command.command_name] = command

    def run(self):
        if self.command:
            self._execute_command(self.command)
        else:
            print(self._main_help(self.commands))
