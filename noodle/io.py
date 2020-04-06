import sys

from ._hue import blue, red, green, yellow
from ._messages import ErrorMsg


class Output:
    def __init__(self, text):
        self.output_to_console(text)

    def output_to_console(self, text):
        print(text)

    @staticmethod
    def warning(text):
        print(yellow(text))

    @staticmethod
    def danger(text):
        print(red(text))

    @staticmethod
    def success(text):
        print(green(text))

    @staticmethod
    def info(text):
        print(blue(text))


class Ask:
    @staticmethod
    def any(text):
        return input(text)

    @staticmethod
    def integer(integer):
        try:
            number = input(integer)
            int(number)
            return number
        except ValueError:
            print(ErrorMsg.wrong_answer(number, int))
            sys.exit()
