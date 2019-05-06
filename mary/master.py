import sys

from .parser import _parse_cli_description


class Master:
    """
    Global CLI configuration
    """

    def __init__(self):
        self.command = self.get_command()
        self.commands = []

    def main_help(cls, commands):
        """
        Generate the Info message for the CLI app.
        """
        if cls.__doc__:
            help_msg = _parse_cli_description(cls.__doc__, commands)
            print(help_msg)

        return "No description yet"

    def get_command(self):
        try:
            return sys.argv[1]
        except IndexError:
            pass

    def execute_command(self, command):
        {com() for com in self.commands if com.__name__ == command}

    def register(self, commands: list):
        """
        Register all the commands.
        """
        [self.commands.append(command) for command in commands]

    def run(self):
        if self.command:
            self.execute_command(self.command)
        else:
            self.main_help(self.commands)


# test comment
