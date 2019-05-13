import pytest

from noodle._messages import ErrorMsg, CliMsg, DescriptionMsg


@pytest.mark.parametrize(
    "command, output",
    [
        ("-test", f"FlagNotFound: '-test' is not registered."),
        ("test", "CommandNotFound: 'test' is not registered."),
    ],
)
def test_wrong_command(command, output):
    msg = ErrorMsg.wrong_command(command)
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
