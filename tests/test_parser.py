from noodle._parser import Parser, _options
from noodle.core import _GLOBAL_OPTIONS

parser = Parser()


def parsed_arguments(arguments):
    return parser.parse_arguments(arguments)


def test_parse_arguments():
    parsed_args = parsed_arguments(["test.py"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands is None
    assert parsed_args.options == []
    assert parsed_args.arguments == []

    # CLI and command
    parsed_args = parsed_arguments(["test.py", "greet"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands == "greet"
    assert parsed_args.options == []
    assert parsed_args.arguments == []

    # CLI, command and argument
    parsed_args = parsed_arguments(["test.py", "greet", "carlos"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands == "greet"
    assert parsed_args.options == []
    assert parsed_args.arguments == ["carlos"]

    # CLI, and a flag
    parsed_args = parsed_arguments(["test.py", "-v"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands is None
    assert parsed_args.options == ["-v"]
    assert parsed_args.arguments == []

    # CLI, and a flag
    parsed_args = parsed_arguments(["test.py", "--version"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands is None
    assert parsed_args.options == ["--version"]
    assert parsed_args.arguments == []

    # CLI, and flags
    parsed_args = parsed_arguments(["test.py", "-v", "--version"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands is None
    assert parsed_args.options == ["-v", "--version"]
    assert parsed_args.arguments == []

    # CLI, command and flag
    parsed_args = parsed_arguments(["test.py", "greet", "-v"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands == "greet"
    assert parsed_args.options == ["-v"]
    assert parsed_args.arguments == []

    # CLI, command, flag and argument
    parsed_args = parsed_arguments(["test.py", "greet", "-y", "carlos"])
    assert parsed_args.name == "test.py"
    assert parsed_args.commands == "greet"
    assert parsed_args.options == ["-y"]
    assert parsed_args.arguments == ["carlos"]


def get_setup(arguments):
    """Simple setup for the get_xxx properties"""
    return Parser(test=True, test_argv=arguments)


def test_get_command():
    parser = get_setup(["test.py", "greet"])
    command = parser.get_command
    assert command == "greet"


def test_get_argument():
    parser = get_setup(["test.py", "greet", "carlos"])
    command = parser.get_argument
    assert command == ["carlos"]


def test_get_options():
    parser = get_setup(["test.py", "-v"])
    command = parser.get_options
    assert command == ["-v"]

    parser = get_setup(["test.py", "--version"])
    command = parser.get_options
    assert command == ["--version"]

    parser = get_setup(["test.py", "--version", "-v"])
    command = parser.get_options
    assert command == ["--version", "-v"]

    parser = get_setup(["test.py", "greet", "-y"])
    command = parser.get_options
    assert command == ["-y"]

    parser = get_setup(["test.py", "greet", "--yell"])
    command = parser.get_options
    assert command == ["--yell"]

    parser = get_setup(["test.py", "greet", "-s", "--yell"])
    command = parser.get_options
    assert command == ["-s", "--yell"]


def test_get_app_name():
    parser = get_setup(["test.py", "greet", "carlos"])
    command = parser.get_app_name
    assert command == "test.py"


def test_parse_options():
    parsed_options = parser.parse_options(_GLOBAL_OPTIONS)
    assert isinstance(parsed_options, list)

    # assert that every one of the options is an
    # instance of the `_options` class.
    for option in parsed_options:
        assert isinstance(option, _options)

    # assert the default version option
    assert parsed_options[0].name == "version"
    assert parsed_options[0].long_flag == "--version"
    assert parsed_options[0].short_flag == "-v"
    assert parsed_options[0].description == "Display this application version"

    # assert the default help option
    assert parsed_options[1].name == "help"
    assert parsed_options[1].long_flag == "--help"
    assert parsed_options[1].short_flag == "-h"
    assert parsed_options[1].description == "Display this help message"
