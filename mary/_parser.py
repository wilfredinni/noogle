from ._messages import CliMsg


def _parse_cli_description(description, commands=None):
    usage = CliMsg.usage()
    app_description = f"{description}\n" f"\nUsage:" f"\n  {usage}"

    if commands:
        app_description += "\n\nCommands:"
        for name, command in commands.items():
            if command.__doc__:
                command_help = command.__doc__.strip()
            else:
                command_help = "No description yet"

            app_description += f"\n  {name.ljust(15)} {command_help}"

    return app_description


def _parse_command_help(description, command, command_name):
    usage = CliMsg.usage(command_name)

    command_description = (
        f"Help:\n" f"  {description}\n" f"\nUsage:\n" f"  {usage}\n" f"\nArguments:"
    )

    for com, description in command.items():
        command_description += f"\n  {com.ljust(15)} {description}"

    return command_description
