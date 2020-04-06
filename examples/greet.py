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
        self.options["age"] = "what is your age"
        return self.options

    def handler(self):
        text = f"hello {self.argument}"

        if self.option("yell") and self.option("shh"):
            text += " Yelled and Shhed"

        if self.option("yell"):
            text = text.upper()

        if self.option("shh"):
            text = text.lower()

        if self.option("age"):
            age = noodle.ask.integer("What is your age? ")
            text += f" , tienes {age}"

        noodle.output.info(text)
        # noodle.output(text)
        # noodle.output.info(text)
        # noodle.output.warning(text)
        # noodle.output.danger(text)
        # noodle.output.success(text)


app = Main()
app.register(Greet)

if __name__ == "__main__":
    app.run()
