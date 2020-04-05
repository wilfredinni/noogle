"""
Very basic example that show how to build the simples CLI.
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
        my_options = {}
        my_options['yell'] = 'Yell in uppercase letters'
        my_options['shh'] = 'Shh in lowercase letters'
        return my_options

    def handler(self):
        text = f"hello {self.argument}"

        if self.option("yell"):
            text = text.upper()

        if self.option('shh'):
            text = text.lower()

        noodle.output(text)


app = Main()
app.register(Greet)

if __name__ == "__main__":
    app.run()
