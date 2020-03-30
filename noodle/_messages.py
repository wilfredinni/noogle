import os
from ._hue import red, orange


class ErrorMsg:
    @staticmethod
    def wrong_command(command):
        return (f"{red('CommandNotFound:')} '{command}' is not a registered Command.")

    @staticmethod
    def wrong_option(option):
        return f"{red('OptionNotFound:')} '{option}' is not a valid option."

    @staticmethod
    def no_argument(argument):
        return f"{red('ArgumentNeeded:')} '{argument}' is required for this command."

    @staticmethod
    def too_many_arguments(command):
        return f"{red('TooManyArguments:')} [{command} -h] for more information."


class CliMsg:
    @staticmethod
    def usage(command_name="command"):
        return f"{command_name} [options] [arguments]"

    @staticmethod
    def version(app_name, version):
        return f"{app_name} v{version}"


class DescriptionMsg:
    @staticmethod
    def no_description(command_name=None):
        if command_name:
            return f"Command '{command_name}' has no description yet{os.linesep}"

        return f"{orange('No description yet')}{os.linesep}"
