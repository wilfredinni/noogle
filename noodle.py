import sys

global_options = {
    "long_options": ["--help", "--version"],
    "short_options": ["-h", "-v"],
}

parameters = [
    {
        "command": "hello",
        "long_options": ["--yell", "--shh"],
        "short_options": ["-s", "-y"],
    },
    {
        "command": "byeee",
        "long_options": ["--yell", "--shh"],
        "short_options": ["-s", "-y"],
    },
]

command_line_parameters = sys.argv

first_parameter = command_line_parameters[1]
# check for global options
if first_parameter.startswith("-"):
    if first_parameter in global_options["long_options"]:
        print("long paramenter passed")
    elif first_parameter in global_options["short_options"]:
        print("short option passed")
    else:
        print("wrong option")

# check for command
else:
    for command in
