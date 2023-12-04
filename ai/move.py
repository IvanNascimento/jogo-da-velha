import random
from difficulty import Difficulty


def available(game_map):
    result = []
    for row in game_map:
        for col in row:
            if col == -1:
                result.append((row, col))
    return result


def easy(game_map: list):
    pass


def medium(game_map: list):
    pass


def hard(game_map: list):
    pass


def randoly(game_map: list):
    availables = available(game_map)
    position = random.choice(range(len(availables)))
    return availables[position]


def play(game_map: list, difficulty=Difficulty.RANDOM):
    match difficulty:
        case Difficulty.EASY:
            return easy(game_map)
        case Difficulty.MEDIUM:
            return medium(game_map)
        case Difficulty.HARD:
            return hard(game_map)
        case _:
            return randoly(game_map)
