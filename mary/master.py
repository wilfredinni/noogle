import sys

from .parser import _parse_cli_description


class Master:
    """
    Global CLI configuration
    """

    def __init__(self):
        self.description = self.cli_description()
        self.command = self.get_command()
        self.commands = []

    def cli_description(cls):
        """
        Generate the Info message for the CLI app.
        """
        if cls.__doc__:
            return _parse_cli_description(cls.__doc__)

    def get_command(self):
        try:
            return sys.argv[1]
        except IndexError:
            return None

    def register(self, commands: list):
        """
        Register all the commands.
        """
        [self.commands.append(command) for command in commands]

    def run(self):
        if self.command:
            for com in self.commands:
                if com.__name__ == self.command:
                    return self.commands[self.commands.index(com)]()
        else:
            if self.description:
                print(self.description)
