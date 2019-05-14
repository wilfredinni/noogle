from ._messages import CliMsg, DescriptionMsg

ls = "  "  # left space for printing


def get_master_help(description, commands, options=None, user_options=None):
    """Returns nicely formatted string with the definition, usage,
    commands and options of a CLI.
    """
    usage = CliMsg.usage()
    app_description = f"{description}\n\n"
    app_description += f"Usage:\n"
    app_description += f"{ls}{usage}"

    if options:
        app_description += formatted_options("\nGlobal Options", options)

    if user_options:
        app_description += formatted_options("Options", user_options)

    if len(commands) > 0:
        app_description += formatted_commands(commands)

    return app_description


def get_command_help(description, argument, command_name, options):
    """Returns nicely formatted string with the definition, command
    description and options of a single command."""
    usage = CliMsg.usage(command_name)

    command_description = f"Help:\n"
    command_description += f"{ls}{description}\n"
    command_description += f"\nUsage:\n  {usage}\n"

    if options:
        command_description += formatted_options("Options", options)

    if argument:
        command_description += formatted_arguments(argument)

    return command_description


def formatted_options(title, options):
    """Returns a multiline string with nice formating for the default
    and user defined options. Part of the Master and Command help.
    """
    fmt_options = f"\n{title}:\n"
    for option in options:
        fmt_options += (
            f"{ls}{option.short_flag}, "
            f"{option.long_flag.ljust(13)}"
            f"{option.description}\n"
        )

    return fmt_options


def formatted_commands(commands):
    """Returns a multiline string with nice formating for all the
    registered commands.
    """
    fmt_commands = "\nCommands:"
    for name, command in commands.items():
        if command.__doc__:
            command_help = command.__doc__.strip()
        else:
            command_help = DescriptionMsg.no_description()

        fmt_commands += f"\n{ls}{name.ljust(16)}"
        fmt_commands += f"{command_help}"

    return fmt_commands


def formatted_arguments(argument):
    """Returns a multiline string with nice formating for all the
    arguments.
    """
    fmt_arguments = f"\nArguments:"
    for name, description in argument.items():
        fmt_arguments += f"\n{ls}{name.ljust(16)} {description}"

    return fmt_arguments
