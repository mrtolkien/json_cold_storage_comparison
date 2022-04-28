import os
import json

import zstandard
import diskcache

import time
import json


class ZSTDDisk(diskcache.Disk):
    def __init__(self, directory, compress_level=15, **kwargs):
        self.compressor = zstandard.ZstdCompressor(level=compress_level)
        self.decompressor = zstandard.ZstdDecompressor()

        super(ZSTDDisk, self).__init__(directory, **kwargs)

    def put(self, key):
        json_bytes = json.dumps(key).encode("utf-8")
        data = self.compressor.compress(json_bytes)

        return super(ZSTDDisk, self).put(data)

    def get(self, key, raw):
        data = super(ZSTDDisk, self).get(key, raw)

        return json.loads(self.decompressor.decompress(data).decode("utf-8"))

    def store(self, value, read, key="UNKNOWN"):
        if not read:
            json_bytes = json.dumps(value).encode("utf-8")
            value = self.compressor.compress(json_bytes)

        return super(ZSTDDisk, self).store(value, read, key=key)

    def fetch(self, mode, filename, value, read):
        data = super(ZSTDDisk, self).fetch(mode, filename, value, read)
        if not read:
            data = json.loads(self.decompressor.decompress(data).decode("utf-8"))

        return data


cache = diskcache.Cache("diskcache_zstd", disk=ZSTDDisk, disk_compress_level=15)


def dump_diskcache_zstd() -> float:
    # Emptying the cache first
    cache.clear()

    start = time.time()

    for file in os.listdir("raw"):
        with open(f"raw/{file}", "r") as match_file:
            data = json.load(match_file)

        cache.set(file, data)

    end = time.time()

    return end - start


def read_diskcache_zstd() -> float:
    start = time.time()

    for file in os.listdir("raw"):
        data = cache.get(file)
        assert data

    end = time.time()

    return end - start
