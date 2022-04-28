import os
import shutil
import zstandard

import time


def dump_zstd() -> float:
    # Emptying the folder first
    try:
        shutil.rmtree("zstd")
    except FileNotFoundError:
        pass

    compressor = zstandard.ZstdCompressor(level=3)

    os.makedirs("zstd")

    start = time.time()

    for file in os.listdir("raw"):
        with open(f"raw/{file}", "r") as match_file:
            data = bytearray(match_file.read(), "utf-8")

        with open(f"zstd/{file}.zst", "wb+") as file:
            file.write(compressor.compress(data=data))

    end = time.time()

    return end - start


def dump_zstd_dict() -> float:
    # Emptying the folder first
    try:
        shutil.rmtree("zstd_dict")
    except FileNotFoundError:
        pass

    os.makedirs("zstd_dict")

    # # We take some time to create the dictionary first
    # samples = []

    # for file in os.listdir("raw"):
    #     with open(f"raw/{file}", "r") as match_file:
    #         samples.append(bytearray(match_file.read(), "utf-8"))

    # compression_dict = zstandard.train_dictionary(1000 * 1000, samples=samples)

    dict_data = None

    start = time.time()

    for file in os.listdir("raw"):
        with open(f"raw/{file}", "r") as match_file:
            data = bytearray(match_file.read(), "utf-8")

        if not dict_data:
            dict_data = zstandard.ZstdCompressionDict(data)
            compressor = zstandard.ZstdCompressor(level=3, dict_data=dict_data)

        with open(f"zstd_dict/{file}.zst", "wb+") as file:
            file.write(
                compressor.compress(
                    data=data,
                )
            )

    end = time.time()

    return end - start
