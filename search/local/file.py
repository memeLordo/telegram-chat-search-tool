import os


class File:
    def __new__(cls):
        cls.index = 1

    @staticmethod
    def mkdir(dirname: str) -> str:
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        return dirname

    @classmethod
    def convert_txt(cls, text: str):
        dir = File.mkdir("./requests")
        filename = f"{dir}/request[{cls.index}].txt"
        while os.path.exists(filename):
            cls.index += 1
            filename = f"{dir}/request[{cls.index}].txt"
        with open(filename, "w+") as file:
            file.write(text)
        cls.index += 1
        print("Файл сохранён.")
