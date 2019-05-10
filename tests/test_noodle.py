from noodle import __version__
from noodle._parser import Parser

parser = Parser()


def test_version():
    assert __version__ == "0.0.1"


# _parser

