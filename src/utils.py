import json
import random

def get_random_triple(file_path):
    # Leggi il file JSON
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Scegli una tripla casuale
    random_entry = random.choice(data)
    
    # Restituisci i dati
    return random_entry["setting"], random_entry["character"], random_entry["goal"]


