"""
Very basic example that show how to build a simple CLI.
"""
import noodle


class Main(noodle.Master):
    """
    Simple CLI app written with Noodle.
    """

    app_name = "Simplest"  # if not specified, defaults to the filename
    version = "0.1.1"  # if not specified, defaults to 0.1.0


class Greet(noodle.Command):
    """
    Greets someone
    """

    command_name = "greet"
    arguments = {"name": "Who do you want to greet?"}
    options = {
        "yell": "Yell in uppercase letters",
        "shh": "Shh in lowercase letters",
    }

    def handler(self):
        greet = f"Hello {self.arguments}"

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
