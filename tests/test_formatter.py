from noodle._formatter import formatted_options, formatted_arguments, formatted_commands
from noodle._parser import Parser
from noodle.core import _GLOBAL_OPTIONS

parser = Parser()


class TestCommand1:
    """command description"""

    command_name = "test_command1"


class TestCommand2:
    command_name = "test_command2"


def test_formatted_options():
    # random test
    options_1 = {"test": "test help"}
    parsed_options = parser.parse_options(options_1)
    fmt_opt = formatted_options("Options", parsed_options)
    lines = fmt_opt.splitlines()
    assert lines[0] == ""
    assert lines[1] == "Options:"
    assert lines[2] == "  -t, --test       test help"

    # global options
    parsed_options = parser.parse_options(_GLOBAL_OPTIONS)
    fmt_opt = formatted_options("Global Options", parsed_options)
    lines = fmt_opt.splitlines()
    assert lines[0] == ""
    assert lines[1] == "Global Options:"
    assert lines[2] == "  -v, --version    Display this application version"
    assert lines[3] == "  -h, --help       Display this help message"


def test_formatted_commands():
    _commands = {}
    _commands.setdefault(TestCommand1.command_name, TestCommand1)
    _commands.setdefault(TestCommand2.command_name, TestCommand2)
    fmt_commands = formatted_commands(_commands)
    lines = fmt_commands.splitlines()
    assert lines[0] == ""
    assert lines[1] == "Commands:"
    assert lines[2] == "  test_command1   command description"
    assert lines[3] == "  test_command2   No description yet"


def test_formatted_arguments():
    argument = formatted_arguments({"test": "test help"}).splitlines()
    assert argument[0] == ""
    assert argument[1] == "Arguments:"
    assert argument[2] == "  test             test help"
