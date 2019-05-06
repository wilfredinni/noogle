def _parse_cli_description(doc, commands=None):
    app_doc = doc.strip()
    usage = "command [options] [arguments]"
    app_description = f"{app_doc}\n" f"\nUsage:" f"\n  {usage}"

    if commands:
        app_description += "\n\nCommands"
        for command in commands:
            app_description += f"\n  {command.command_name} - {command.__doc__.strip()}"

    return app_description


def _parse_command_help(doc, command, command_name):
    usage = f"{command_name} [options] [arguments]"
    app_doc = doc.strip()

    command_description = (
        f"Help:\n" f"  {app_doc}\n" f"\nUsage:\n" f"  {usage}\n" f"\nArguments:"
    )

    for com, description in command.items():
        command_description += f"\n  {com} - {description}"

    return command_description
