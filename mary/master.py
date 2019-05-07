import sys

from ._messages import ErrorMsg, DescriptionMsg
from ._parser import _parse_cli_description


class Master:
    """
    Global CLI configuration
    """

    def __init__(self):
        self.command = self._get_command()
        self.commands = []

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
        com = {com for com in self.commands if com.__name__ == command}
        if com:
            return list(com)[0]()

        print(ErrorMsg.wrong_command(command))

    def register(self, commands: list):
        """
        Register all the commands.
        """
        [self.commands.append(command) for command in commands]

    def run(self):
        if self.command:
            self._execute_command(self.command)
        else:
            print(self._main_help(self.commands))
