def _parse_cli_description(doc, commands=None):
    app_doc = doc.strip()
    usage = "command [options] [arguments]"
    app_description = f"{app_doc}\n" f"\nUsage:" f"\n  {usage}"

    if commands:
        app_description += "\n\nCommands"
        for command in commands:
            app_description += f"\n  {command.command_name} - {command.__doc__.strip()}"

    return app_description


def _parse_command_help(doc, command):
    app_doc = doc.strip()

    # TODO fix the "name", must be the command name
    usage = f"{command} [options] [arguments]"

    command_description = (
        f"Help:\n"
        f"  {app_doc}\n"
        f"\nUsage:\n"
        f"  {usage}\n"
        f"\nArguments:"
        # f"  {command} - {help}"
    )

    # for command in commands:
    for c, h in command.items():
        command_description += f"\n  {c} - {h}"

    return command_description
