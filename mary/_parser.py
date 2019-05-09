import sys
from collections import namedtuple

_options = namedtuple("options", ["name", "long_flag", "short_flag", "description"])


class Parser:
    def __init__(self):
        self.argvs = sys.argv

        self.cli_name = None
        self.commands = []
        self.arguments = []

        # get the information
        self.get_elements(self.argvs)

    def get_elements(self, argvs):
        if len(argvs) > 1:
            self.commands.append(argvs[1])

        if len(argvs) > 2:
            self.arguments.append(argvs[2])

    def get_command(self):
        if len(self.commands) > 0:
            return self.commands[0]

    def get_argument(self):
        if len(self.arguments) > 0:
            return self.arguments[0]

    def get_options(self, options):
        """
        Parse a dictionary containing Master or Command options.

        Arguments:
            options Dict -- {"name": "description"}

        Returns:
            List -- List of namedtuple objects
        """
        parsed_options = []
        for name, description in options.items():
            name = name
            long_flag = f"--{name}"
            short_flag = f"-{name[0]}"
            description = description
            parsed_options.append(_options(name, long_flag, short_flag, description))

        return parsed_options
