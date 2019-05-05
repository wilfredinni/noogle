import sys

from .parser import _parse_cli_description, _parse_command_help


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
                    self.commands[self.commands.index(com)]()
        else:
            if self.description:
                print(self.description)


class Command:
    help = None

    def __init__(self):
        self.description = self.command_description()
        self.argument = self.get_argument()

        if self.argument:
            self.handler()

    def command_description(cls):
        """
        Generate the help message.
        """
        arg = "name"  # TODO: get the argument dinamically
        if cls.__doc__:
            return _parse_command_help(cls.__doc__, arg, cls.help)

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
