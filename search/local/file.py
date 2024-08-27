import os


def mkdir(dirname: str) -> str:
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    return dirname


def save_to_txt(text: str):
    global index
    dir = mkdir("./requests")
    filename = f"{dir}/request[{index}].txt"
    while os.path.exists(filename):
        index += 1
        filename = f"{dir}/request[{index}].txt"
    with open(filename, "w+") as file:
        file.write(text)
    index += 1
    print("Файл сохранён.")
