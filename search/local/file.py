import os


class File:
    def __init__(self):
        self.index = 1

    @staticmethod
    def mkdir(dirname: str) -> str:
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return dirname

    def convert_txt(self, text: str):
        dir = File.mkdir("./requests")
        filename = f"{dir}/request[{self.index}].txt"
        while os.path.exists(filename):
            self.index += 1
            filename = f"{dir}/request[{self.index}].txt"
        with open(filename, "w+") as file:
            file.write(text)
        self.index += 1
        print("Файл сохранён.")
