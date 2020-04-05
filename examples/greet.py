"""
Very basic example that show how to build a simple CLI.
"""
import noodle


class Main(noodle.Master):
    """
    Sample CLI app written with Noodle.
    """

    app_name = "Noodle"
    version = "0.1.2"


class Greet(noodle.Command):
    """
    Greets someone
    """

    command_name = "greet"
    argument = {"name": "Who do you want to greet?"}

    def command_options(self):
        self.options["yell"] = "Yell in uppercase letters"
        self.options["shh"] = "Shh in lowercase letters"
        return self.options

    def handler(self):
        text = f"hello {self.argument}"

        if self.option("yell"):
            text = text.upper()

        if self.option("shh"):
            text = text.lower()

        noodle.output(text)


class SayBye(noodle.Command):
    """
    Say bye to someone
    """

    command_name = "bye"
    argument = {"name": "Who do you want to say bye?"}

    def command_options(self):
        self.options["yell"] = "Yell in uppercase letters"
        self.options["shh"] = "Shh in lowercase letters"
        return self.options

    def handler(self):
        text = f"bye {self.argument}"

        if self.option("yell"):
            text = text.upper()

        if self.option("shh"):
            text = text.lower()

        noodle.output(text)


app = Main()
app.register(Greet, SayBye)

if __name__ == "__main__":
    app.run()
