# Noodle

[![Build Status](https://travis-ci.org/wilfredinni/noodle.svg?branch=master)](https://travis-ci.org/wilfredinni/noodle) [![codecov](https://codecov.io/gh/wilfredinni/noodle/branch/master/graph/badge.svg)](https://codecov.io/gh/wilfredinni/noodle) [![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/wilfredinni/mary/blob/master/LICENSE)


Easily create beautiful and lightweight Command Line tools

```python
# cli.py
from noodle import Master, Command


class Main(Master):
    """
    Sample CLI app written with Noodle.
    """


class Greet(Command):
    """
    Greets someone
    """

    command_name = "greet"
    argument = {"name": "Who do you want to greet?"}

    def handler(self):
        print(f"Hello {self.argument}")


app = Main()
app.register(Greet)

if __name__ == "__main__":
    app.run()
```

Calling the script:

```
$ python cli.py
Sample CLI app for the Rose framework.

Usage:
  command [options] [arguments]

Commands:
  greet           Greets someone
```

Calling a command:

```
$ python cli.py greet
Help:
  Greets someone

Usage:
  greet [options] [arguments]

Arguments:
  name            Who do you want to greet?
```

Calling the command and the argument:

```
$ python cli.py greet Charles
Hello Charles
```