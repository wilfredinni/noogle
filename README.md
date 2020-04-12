# Noodle

[![Build Status](https://travis-ci.org/wilfredinni/noodle.svg?branch=master)](https://travis-ci.org/wilfredinni/noodle) [![codecov](https://codecov.io/gh/wilfredinni/noodle/branch/master/graph/badge.svg)](https://codecov.io/gh/wilfredinni/noodle) [![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/wilfredinni/mary/blob/master/LICENSE)


Easily create beautiful and lightweight Command Line tools (WIP)

## Simple Example

```python
# simplest.py
import noodle


class Main(noodle.Master):
    """
    Simple CLI app written with Noodle.
    """

    app_name = "Simplest"  # if not specified, defaults to the file name
    version = "0.1.1"  # if not specified, defaults to 0.1.0


class Greet(noodle.Command):
    """
    Greets someone
    """

    command_name = "greet"
    argument = {"name": "Who do you want to greet?"}
    options = {
        "yell": "Yell in uppercase letters",
        "shh": "Shh in lowercase letters",
    }

    def handler(self):
        greet = f"Hello {self.argument}"

        if self.option("yell"):
            noodle.output.danger(greet.upper())

        elif self.option("shh"):
            noodle.output.info(greet.lower())

        else:
            noodle.output(greet)


app = Main()
app.register(Greet)

if __name__ == "__main__":
    app.run()

```

[![asciicast](https://asciinema.org/a/OUvObO8R6wu4Gt9YUyC0CIwE7.svg)](https://asciinema.org/a/OUvObO8R6wu4Gt9YUyC0CIwE7)
