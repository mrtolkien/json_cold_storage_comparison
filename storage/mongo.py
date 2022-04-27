from pymongo import MongoClient
import time
import json
import os

client = MongoClient("mongodb://localhost:27017")
database = client["lol_dump"]
collection = database["matches"]


def dump_mongo() -> float:
    collection.drop()

    start = time.time()

    for file in os.listdir("raw"):
        with open(f"raw/{file}", "r") as match_file:
            data = json.load(match_file)

        data["_id"] = file

        collection.insert_one(data)

    end = time.time()

    return end - start


def read_mongo() -> float:
    start = time.time()

    for file in os.listdir("raw"):
        data = collection.find_one(file)
        assert data

    end = time.time()

    return end - start
