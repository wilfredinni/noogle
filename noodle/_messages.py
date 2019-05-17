class ErrorMsg:
    @staticmethod
    def wrong_command(command):
        return f"CommandNotFound: '{command}' is not registered."

    @staticmethod
    def wrong_option(option):
        return f"OptionNotFound: '{option}' is not a valid option."

    @staticmethod
    def no_argument(argument):
        return f"ArgumentNeeded: '{argument}' is a mandatory argument for this command."

    @staticmethod
    def too_many_arguments(command):
        return f"TooManyArguments: [{command} -h] for more information."


class CliMsg:
    @staticmethod
    def usage(command_name="command"):
        return f"{command_name} [options] [arguments]"

    @staticmethod
    def version(app_name, version):
        return f"{app_name} {version}"


class DescriptionMsg:
    @staticmethod
    def no_description(command_name=None):
        if command_name:
            return f"Command '{command_name}' has no description yet"

        return "No description yet"
