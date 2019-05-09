import sys
from collections import namedtuple

_argv = namedtuple("argvs", ["name", "commands", "flags", "arguments"])
_options = namedtuple("options", ["name", "long_flag", "short_flag", "description"])


class Parser:
    def __init__(self):
        self.argv = sys.argv
        self.parsed_argv = self.parse()

    def parse(self):
        name = self.argv[0]
        commands = None

        if len(self.argv) > 1:
            commands = self.argv[1]

        flags = [arg for arg in self.argv if arg.startswith("-")]
        arguments = [arg for arg in self.argv[2:] if not arg.startswith("-")]

        print(_argv(name, commands, flags, arguments))

        return _argv(name, commands, flags, arguments)

    def get_command(self):
        return self.parsed_argv.commands

    def get_argument(self):
        return self.parsed_argv.arguments

    def get_flags(self):
        return self.parsed_argv.flags

    def get_app_name(self):
        return self.parsed_argv.name

    def parse_options(self, options):
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
