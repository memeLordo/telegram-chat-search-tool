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
