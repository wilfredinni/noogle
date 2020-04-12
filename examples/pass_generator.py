"""
Very basic example that show how to build a simple CLI.
"""
import noodle


class Main(noodle.Master):
    """
    Easily generate strong passwords.
    """

    app_name = "Password Generator"
    version = "0.1.0"


class Generate(noodle.Command):
    """
    Generate a strong password
    """

    command_name = "generate"
    argument = {"string": "The base string for the password"}
    # options = {}
    # options["yell"] = "Yell in uppercase letters"
    # options["shh"] = "Shh in lowercase letters"
    # options["age"] = "what is your age"

    # def command_options(self):
        # self.options["yell"] = "Yell in uppercase letters"
        # self.options["shh"] = "Shh in lowercase letters"
        # self.options["age"] = "what is your age"

        # self.options["password"] = {
        #     "help": "Yell in uppercase letters",
        #     "type": "password",
        #     "input": True
        # }

        # return self.options

    def handler(self):
        noodle.output.info("Comming soon...")


app = Main()
app.register(Generate)

if __name__ == "__main__":
    app.run()
