from typing import Union, IO

POSSIBILITIES = [
    "XMAS",
    "MXAS",
    "MAXS",
    "MASX",

    "XAMS",
    "XASM",

    "AXMS",
    "XAMS",
    "XMSA",

    "SXMA",
    "XSMA",
    "XMSA",
]


def file_handler(file_name: str) -> Union[IO, Exception]:
    try:
        file = open(file_name, "r")
        return file
    except (FileNotFoundError, IOError) as e:
        print("exception was raised while opening the file")
        return e

    pass


def read_file(file_name: str) -> None:
    file = file_handler(file_name)

    if isinstance(file, Exception):
        print(f"\nAn error occured:\n{file} ")
        return

    lines = [line.rstrip() for line in file.readlines()]
    print(lines)

    for line in lines:
        for p in POSSIBILITIES:
            if p in line:
                print(f":MATCHA {line}, {p}")
            


# for each line we need to be able run it through possiblities
read_file("./day4.txt")

# [expression for item in iterable if condition]
