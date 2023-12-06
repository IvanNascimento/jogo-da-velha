import random

def _available(game_map):
    result = []
    for row in range(3):
        for col in range(3):
            if game_map[row][col] == -1:
                result.append((row, col))
    return result


def _easy(game_map):
    #100 jogos
    return (-1,-1)


def _medium(game_map):
    # 500
    pass


def _hard(game_map):
    # 1000
    pass


def _randoly(game_map):
    availables = _available(game_map)
    position = random.choice(range(len(availables)))
    return availables[position]


def play(game_map, difficulty=0):
    if difficulty == 1:
        return _easy(game_map)
    elif difficulty == 2:
        return _medium(game_map)
    elif difficulty == 3:
        return _hard(game_map)
    else:
        return _randoly(game_map)
