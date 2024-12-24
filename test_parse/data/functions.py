import os


def read_file(file_name: str = "data/ansers.txt") -> list[str]:
    if os.path.exists(file_name):
        with open(file__name, "w"):
            pass

    with open(file_name, "r", encoding="utf-8") as file:
        pizzas = file.readlines()
    return pizzas


def write_file(pizza, file_name: str = "data/answers.txt") -> None:
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(pizza + "\n")