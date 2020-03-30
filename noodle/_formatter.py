import os

from ._messages import CliMsg, DescriptionMsg
from ._hue import cyan, bold


def cyan_title(text):
    return f"{os.linesep}{bold(cyan(text))}{os.linesep}"


def get_master_help(description, commands, options=None, user_options=None):
    """
    Returns a nicely formatted string with the definition, usage,
    commands and options of the CLI.
    """
    cli_description = f"{description}"
    cli_description += f"{cyan_title('USAGE')}"
    cli_description += f"{CliMsg.usage()}"

    if options:
        cli_description += formatted_options(
            options, f"{cyan_title('OPTIONS')}"
        )

    if user_options:
        cli_description += formatted_options(user_options)

    if len(commands) > 0:
        cli_description += f"{formatted_commands(commands)}{os.linesep}"

    return cli_description


def get_command_help(description, argument, command_name, options, user_options):
    """
    Returns a nicely formatted string with the definition, command
    description and options of a single command.
    """
    usage = CliMsg.usage(command_name)
    command_description = f"{description}"
    command_description += f"{cyan_title('USAGE')}"
    command_description += f"{usage}"

    command_description += formatted_options(options, f"{cyan_title('OPTIONS')}")
    if user_options:
        command_description += formatted_options(user_options)

    if argument:
        command_description += f"{formatted_arguments(argument)}{os.linesep}"

    return command_description


def formatted_options(options, title=None):
    """
    Returns a multiline string with nice formating for the default
    and user defined options. Part of the Master and Command help.
    """
    fmt_options = f"{os.linesep}{title}" if title else ""
    for option in options:
        fmt_options += f"{option.short_flag}, "
        fmt_options += f"{option.long_flag.ljust(13)}"
        fmt_options += f"{option.description}{os.linesep}"

    return fmt_options


def formatted_commands(commands):
    """
    Returns a multiline string with nice formating for all the
    registered commands.
    """
    fmt_commands = f"{cyan_title('COMMANDS')}"
    for name, command in commands.items():
        doc = command.__doc__
        command_help = doc.strip() if doc else DescriptionMsg.no_description()
        # if command.__doc__:
        #     command_help = command.__doc__.strip()
        # else:
        #     command_help = DescriptionMsg.no_description()

        fmt_commands += f"{name.ljust(17)}"
        fmt_commands += f"{command_help}"

    return fmt_commands


def formatted_arguments(argument):
    """
    Returns a multiline string with nice formating for all the
    arguments.
    """
    fmt_arguments = f"{cyan_title('ARGUMENTS')}"
    for name, description in argument.items():
        fmt_arguments += f"{name.ljust(16)} {description}"

    return fmt_arguments
