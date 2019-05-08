class ErrorMsg:
    @staticmethod
    def wrong_command(command):
        return f"CommandNotFound: '{command}' is not registered."


class CliMsg:
    @staticmethod
    def usage(command_name="command"):
        return f"{command_name} [options] [arguments]"


class DescriptionMsg:
    @staticmethod
    def no_description(command_name=None):
        if command_name:
            return f"Command '{command_name}' has no description yet"

        return "No description yet"
