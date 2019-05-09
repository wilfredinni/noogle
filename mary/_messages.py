class ErrorMsg:
    @staticmethod
    def wrong_command(argument):
        if argument.startswith("-"):
            return f"FlagNotFound: '{argument}' is not registered."

        return f"CommandNotFound: '{argument}' is not registered."


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
