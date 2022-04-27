import os
import json

import diskcache

import time


cache = diskcache.FanoutCache("diskcache")


def dump_diskcache() -> float:
    # Emptying the cache first
    cache.clear()

    start = time.time()

    for file in os.listdir("raw"):
        with open(f"raw/{file}", "r") as match_file:
            data = json.load(match_file)

        cache.set(file, data)

    end = time.time()

    return end - start


def read_diskcache() -> float:
    start = time.time()

    for file in os.listdir("raw"):
        data = cache.get(file)
        assert data

    end = time.time()

    return end - start
