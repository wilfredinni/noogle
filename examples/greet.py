"""
Very basic example that show how to build the simples CLI.
"""
import noodle


class Main(noodle.Master):
    """
    Sample CLI app written with Noodle.
    """

    app_name = "Greet App"
    version = "0.1.2"


class Greet(noodle.Command):
    """
    Greets someone
    """

    command_name = "greet"
    argument = {"name": "Who do you want to greet?"}
    options = {"yell": "Yell in uppercase letters"}

    def handler(self):
        text = f"hello {self.argument}"

        if self.option("yell"):
            text = text.upper()

        noodle.output(text)


app = Main()
app.register(Greet)

if __name__ == "__main__":
    app.run()
