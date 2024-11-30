import json
import random
from typing import Tuple


def get_random_triple(file_path) -> Tuple[str, str, str]:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        random_entry = random.choice(data)

        return random_entry["setting"], random_entry["character"], random_entry["goal"]

    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
