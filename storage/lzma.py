import os
import lzma
import json
import shutil

import time


def dump_lzma() -> float:
    # Emptying the folder first
    try:
        shutil.rmtree("lzma")
    except FileNotFoundError:
        pass

    os.makedirs("lzma")

    start = time.time()

    for file in os.listdir("raw"):
        with open(f"raw/{file}", "r") as match_file:
            data = bytearray(match_file.read(), "utf-8")

        with lzma.open(f"lzma/{file}.xz", "w") as file:
            file.write(data)

    end = time.time()

    return end - start


def read_lzma() -> float:
    start = time.time()

    for file in os.listdir("raw"):
        with lzma.open(f"lzma/{file}.xz") as file:
            file_content = file.read()
            assert file_content

    end = time.time()

    return end - start
