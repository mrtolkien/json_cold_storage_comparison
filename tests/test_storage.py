import dotenv
import diskcache
import shutil

import storage

cache = diskcache.Cache("results")


def test_create_storage():
    dotenv.load_dotenv()

    storage.create_raw()


def test_create_diskcache():
    time = storage.dump_diskcache()

    cache.set("dump_diskcache", time)


def test_read_diskcache():
    time = storage.read_diskcache()

    cache.set("read_diskcache", time)


def test_create_mongo():
    time = storage.dump_mongo()

    cache.set("dump_mongo", time)


def test_read_mongo():
    time = storage.read_mongo()

    cache.set("read_mongo", time)
