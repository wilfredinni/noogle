def _parse_cli_description(doc):
    app_doc = doc.strip()
    usage = "command [options] [arguments]"

    app_description = f"""{app_doc}
    \nUsage:
    {usage}
    """

    return app_description
