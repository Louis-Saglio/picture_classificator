import sys
import json
import random
import os


def choice(data, nbr, duplicate=True):
    if not duplicate:
        data = tuple(set(data))
    return [random.choice(data) for _ in range(nbr)]


def raise_error(message, return_code=1):
    sys.stdout.buffer.write(bytes(message, encoding="utf-8"))
    sys.exit(return_code)


def load_json(json_path):
    try:
        with open(json_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise_error(f"Aucun fichier {json_path} trouvé")
    except json.JSONDecodeError:
        raise_error("Json invalide")


def rlistdir(path='.'):
    files_list = []
    for directory, sub_dir, files in os.walk(path):
        for file in files:
            files_list.append(os.path.join(directory, file))
    return files_list
