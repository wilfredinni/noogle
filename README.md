# Mary (tentative name)

Easily create beautiful and lightweight Command Line tools

```python
# cli.py
from mary import Master, Command


class Main(Master):
    """
    Sample CLI app for the Mary framework.
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
app.register([Greet])

if __name__ == "__main__":
    app.run()
```

Calling the script:

```shell
$ python cli.py
Sample CLI app for the Rose framework.

Usage:
  command [options] [arguments]

Commands:
  greet - Greets someone
```

Calling a command:

```shell
$ python cli.py greet
Help:
  Greets someone

Usage:
  greet [options] [arguments]

Arguments:
  name - Who do you want to greet?
```

Calling the command and the argument:

```shell
$ python cli.py Greet Charles
Hello Charles
```