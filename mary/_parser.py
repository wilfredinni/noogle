import sys


class Parser:
    @staticmethod
    def parse(expression):
        argvs = sys.argv

        if expression == "command":
            try:
                return argvs[1]
            except IndexError:
                pass

        elif expression == "argument":
            try:
                return sys.argv[2]
            except IndexError:
                pass
