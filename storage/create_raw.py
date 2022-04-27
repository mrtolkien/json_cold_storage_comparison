import os
import json

import riotwatcher


def create_raw():
    """Creates the raw sources in the /raw directory."""
    os.makedirs("raw", exist_ok=True)

    # We get the last 1000 Faker games
    player_name = "Trayton"
    region = "EUW1"

    watcher = riotwatcher.LolWatcher(os.getenv("LOL_API_KEY"))

    summoner = watcher.summoner.by_name(region, player_name)

    for page in range(10):
        matches = watcher.match.matchlist_by_puuid(
            region=region,
            puuid=summoner["puuid"],
            start=page * 100,
            count=100,
            queue=420,
        )

        for match_id in matches:
            match_filename = f"raw/{match_id}_match.json"

            if os.path.exists(match_filename):
                continue

            match = watcher.match.by_id(region, match_id)
            timeline = watcher.match.timeline_by_match(region, match_id)

            with open(match_filename, "w+") as file:
                json.dump(match, file)

            with open(f"raw/{match_id}_matchtimeline.json", "w+") as file:
                json.dump(timeline, file)
