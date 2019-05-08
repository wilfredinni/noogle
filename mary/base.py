from ._parser import Parser


class Base:
    parse = Parser()

    def _get_doc(cls):
        if cls.__doc__:
            return cls.__doc__.strip()
