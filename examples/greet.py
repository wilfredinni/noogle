"""
Very basic example that show how to build the simples CLI.
"""
from mary import Master, Command


class Main(Master):
    """
    Sample CLI app for the Rose framework.
    """


class Greet(Command):
    """
    Greets someone
    """

    command_name = "greet"
    argument = {"name": "Who do you want to greet?"}

    def handler(self):
        print(f"hello {self.argument}")


app = Main()
app.register(Greet)

if __name__ == "__main__":
    app.run()
