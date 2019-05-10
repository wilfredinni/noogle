from ._messages import CliMsg

ls = "  "  # left space for printing


def get_master_help(description, commands, options=None, user_options=None):
    usage = CliMsg.usage()
    app_description = f"{description}\n\n"
    app_description += f"Usage:\n"
    app_description += f"{ls}{usage}"

    if options:
        app_description += "\n\nGlobal Options:\n"

        for option in options:
            app_description += (
                f"{ls}{option.short_flag}, "
                f"{option.long_flag.ljust(13)}"
                f"{option.description}\n"
            )

    if user_options:
        app_description += "\nOptions:\n"
        for option in user_options:
            app_description += (
                f"{ls}{option.short_flag}, "
                f"{option.long_flag.ljust(13)}"
                f"{option.description}\n"
            )

    if len(commands) > 0:
        app_description += "\nCommands:"
        for name, command in commands.items():
            if command.__doc__:
                command_help = command.__doc__.strip()
            else:
                command_help = "No description yet"

            app_description += f"\n{ls}{name.ljust(16)}"
            app_description += f"{command_help}"

    return app_description


def get_command_help(description, argument, command_name, options):
    usage = CliMsg.usage(command_name)

    command_description = f"Help:\n"
    command_description += f"{ls}{description}\n"
    command_description += f"\nUsage:\n  {usage}\n"

    if options:
        command_description += "\nOptions:\n"

        for option in options:
            command_description += (
                f"{ls}{option.short_flag}, "
                f"{option.long_flag.ljust(13)}"
                f"{option.description}\n"
            )

    if argument:
        command_description += f"\nArguments:"
        for name, description in argument.items():
            command_description += f"\n{ls}{name.ljust(16)} {description}"

    return command_description
