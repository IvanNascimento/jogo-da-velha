import random
from difficulty import Difficulty


def _available(game_map):
    result = []
    for row in range(3):
        for col in range(3):
            if game_map[row][col] == -1:
                result.append((row, col))
    return result


def _easy(game_map: list):
    # 100 jogos
    pass


def _medium(game_map: list):
    # 500
    pass


def _hard(game_map: list):
    # 1000
    pass


def _randoly(game_map: list):
    availables = _available(game_map)
    position = random.choice(range(len(availables)))
    return availables[position]


def play(game_map: list, difficulty=Difficulty.RANDOM):
    match difficulty:
        case Difficulty.EASY:
            return _easy(game_map)
        case Difficulty.MEDIUM:
            return _medium(game_map)
        case Difficulty.HARD:
            return _hard(game_map)
        case _:
            return _randoly(game_map)
