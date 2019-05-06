def _parse_cli_description(doc, commands=None):
    app_doc = doc.strip()
    usage = "command [options] [arguments]"
    app_description = f"{app_doc}\n" f"\nUsage:" f"\n  {usage}"

    if commands:
        app_description += "\n\nCommands"
        for command in commands:
            app_description += f"\n  {command.__name__} - {command.help}"

    return app_description


def _parse_command_help(doc, command, help):
    app_doc = doc.strip()
    usage = f"{command} [options] [arguments]"

    command_description = (
        f"Help:\n"
        f"  {app_doc}\n"
        f"\nUsage:\n"
        f"  {usage}\n"
        f"\nArguments:\n"
        f"  {command} - {help}"
    )

    return command_description
