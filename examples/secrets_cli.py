import string
import secrets

import noodle


class Main(noodle.Master):
    """
    CLI Wrapper around the Python secrets module.
    """

    app_name = "Password Generator"
    version = "0.1.0"


class Password(noodle.Command):
    """
    Generate a ten-character password with lowercases, uppercases and digits.
    """

    command_name = "password"

    def command_options(self):
        self.options["length"] = {
            "help": "Change the character length of the password (10)",
            "default": 10,
        }
        self.options["digits"] = {
            "help": "Change the minimum occurrences of digits (3)",
            "default": 1,
        }
        self.options["punctuation"] = "Add punctuation to the password"
        return self.options

    def handler(self):
        alphabet = string.ascii_letters + string.digits
        if self.option("punctuation"):
            alphabet += string.punctuation

        while True:
            password = "".join(
                secrets.choice(alphabet) for i in range(self.option("length"))
            )
            if (
                sum(c.islower() for c in password) >= 1
                and sum(c.isupper() for c in password) >= 1
                and sum(c.isdigit() for c in password) >= self.option("digits")
            ):
                break

        noodle.output.success(f"Your Password: {password}")


app = Main()
app.register(Password)

if __name__ == "__main__":
    app.run()
