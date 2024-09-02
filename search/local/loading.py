import sys
import time


class Load:
    class Bar:
        symbol = "-"
        length = 50

        def __init__(self, symbol=symbol, length=length):
            self.symbol = symbol
            self.length = length

        def __str__(self) -> str:
            return self.symbol * self.length

    bar = Bar()
    message = f"Loading: [{bar}]"
    backtrack = "\b" * len(message)

    @classmethod
    def create(cls):
        sys.stdout.write(cls.backtrack + cls.message)
        cls.buffer = cls.message

    @classmethod
    def update(cls):
        cls.buffer = cls.buffer.replace(cls.bar.symbol, "=", 1)
        sys.stdout.flush()
        sys.stdout.write(cls.backtrack + cls.buffer)
        time.sleep(1 / cls.bar.length)

