def _parse_cli_description(doc):
    app_doc = doc.strip()
    usage = "command [options] [arguments]"

    app_description = f"""{app_doc}
    \nUsage:
    {usage}
    """

    return app_description


def _parse_command_help(doc, command, help):
    app_doc = doc.strip()
    usage = f"{command} [options] [arguments]"

    command_description = (
        f"Help:\n"
        f"    {app_doc}\n"
        f"\nUsage:\n"
        f"    {usage}\n"
        f"\nArguments:\n"
        f"    {command} - {help}"
    )

    return command_description
