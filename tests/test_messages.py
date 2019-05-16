import pytest

from noodle._messages import ErrorMsg, CliMsg, DescriptionMsg


@pytest.mark.parametrize(
    "command, output", [("test", "CommandNotFound: 'test' is not registered.")]
)
def test_wrong_command(command, output):
    msg = ErrorMsg.wrong_command(command)
    assert msg == output


@pytest.mark.parametrize(
    "option, output",
    [
        ("--test", "OptionNotFound: '--test' is not a valid option."),
        ("-t", "OptionNotFound: '-t' is not a valid option."),
    ],
)
def test_wrong_option(option, output):
    msg = ErrorMsg.wrong_option(option)
    assert msg == output


def test_usage():
    assert CliMsg.usage() == "command [options] [arguments]"
    assert CliMsg.usage("test") == "test [options] [arguments]"


def test_version():
    assert CliMsg.version("test_app", "0.0.1") == "test_app 0.0.1"


def test_no_description():
    assert DescriptionMsg.no_description() == "No description yet"

    msg = DescriptionMsg.no_description("test")
    assert msg == "Command 'test' has no description yet"
