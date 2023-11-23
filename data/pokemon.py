from dataclasses import dataclass
from pathlib import Path
import csv
import config

def isnumber(v):
    try:
        int(v)
    except ValueError:
        return False
    return True

def get_data_from(filename):
    path = Path(__file__).parent / filename

    with open(path) as f:
        reader = csv.DictReader(f)
        data = [
            {k: int(v) if isnumber(v) else v for k, v in row.items()}
            for row in reader
        ]

    return data

def get_pokemon():
    species = [None] + get_data_from("pokemon.csv")
    return [row["name.en"].lower() for row in species[1:] if "enabled" in row]

class DataManager:
    def __init__(self):
        self.pokemon = get_pokemon()
