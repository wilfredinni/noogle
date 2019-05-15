import sys
from collections import namedtuple

_argv = namedtuple("argvs", ["name", "commands", "flags", "arguments"])
_options = namedtuple("options", ["name", "long_flag", "short_flag", "description"])


class Parser:
    def __init__(self, test=False, test_argv=None):
        self.test = test
        self.test_argv = test_argv
        self.parsed_argv = self._arguments

    @property
    def _arguments(self):
        if self.test:
            return self.parse_arguments(self.test_argv)

        return self.parse_arguments(sys.argv)

    def parse_arguments(self, argv):
        """
        Given an iterable of arguments, it returns a namedtuple class with the
        name of the of the script at `parsed_argv.name`, the commands at
        `parsed_argv.commands`, the flags at `parsed_argv.flags` and the rest of
        the arguments at `parsed_argv.arguments`.

        Missing items are filled with `None`.
        """
        name = argv[0]

        commands = None
        if len(argv) > 1 and not argv[1].startswith("-"):
            commands = argv[1]

        flags = [arg for arg in argv if arg.startswith("-")]
        arguments = [arg for arg in argv[2:] if not arg.startswith("-")]

        return _argv(name, commands, flags, arguments)

    @property
    def get_command(self):
        return self.parsed_argv.commands

    @property
    def get_argument(self):
        return self.parsed_argv.arguments

    @property
    def get_flags(self):
        return self.parsed_argv.flags

    @property
    def get_app_name(self):
        return self.parsed_argv.name

    @staticmethod
    def parse_options(options):
        """
        Given an iterable of arguments that represents the default and user
        declared options, it returns a namedtuple class with the name of the
        command at `parsed_options.name`, the full flag at `parsed_options.long_flag`,
        the short flags at `parsed_options.short_flag` and the description at
        `parsed_options.description`.
        """
        parsed_options = []
        for name, description in options.items():
            name = name
            long_flag = f"--{name}"
            short_flag = f"-{name[0]}"
            description = description
            parsed_options.append(_options(name, long_flag, short_flag, description))

        return parsed_options
