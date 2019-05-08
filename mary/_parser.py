import sys


class Parser:
    def __init__(self):
        self.argvs = sys.argv

        self.cli_name = None
        self.commands = []
        self.arguments = []

        # TODO: not implemented yet
        self.options = []

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
