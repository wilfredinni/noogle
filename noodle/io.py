from ._hue import blue, red, green, yellow


def output(string):
    print(string)


class Echo:
    def __init__(self, text):
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
