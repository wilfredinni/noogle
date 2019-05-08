from ._messages import ErrorMsg, DescriptionMsg
from ._formatter import get_master_help
from ._parser import Parser


class Master:
    """
    Global CLI configuration
    """

    def __init__(self):
        self._command = Parser.parse("command")
        self._commands = {}

    def _main_help(cls, commands):
        """
        Generate the Info message for the CLI app.
        """
        if cls.__doc__:
            description = cls.__doc__.strip()
        else:
            description = DescriptionMsg.no_description()

        return get_master_help(description, commands)

    def _execute_command(self, command):
        if command in self._commands.keys():
            return self._commands[command]()

        print(ErrorMsg.wrong_command(command))

    def register(self, commands: list):
        """
        Register all the commands.
        """
        for command in commands:
            self._commands[command.command_name] = command

    def run(self):
        if self._command:
            self._execute_command(self._command)
        else:
            print(self._main_help(self._commands))
