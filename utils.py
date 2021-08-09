import requests
import random


def fetch_pokemon_info(pokemon_id: int, trainer_level: int):
    """
    Returns the name, level and move list given the Pokemon ID and Trainer Level
    """
    request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/")
    request = request.json()
    name = request.get("name")
    level = random.randint(trainer_level - 5, trainer_level + 5)
    moves = request.get("moves")
    suitable_move_list = []
    for move in moves:
        if (
            move.get("version_group_details")[0].get("level_learned_at")
            < level
        ):
            suitable_move_list.append(move.get("move").get("name"))
    move_list = []
    for _ in range(4):
        move_list.append(
            suitable_move_list[random.randint(0, len(suitable_move_list) - 1)]
        )

    return name, level, move_list


def fetch_move_info(move_name):
    """
    Returns the accuracy and power on a move given it's name
    """
    request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{move_name}/")
    request = request.json()
    accuracy = request.get("accuracy")
    power = request.get("power")
    return accuracy, power
