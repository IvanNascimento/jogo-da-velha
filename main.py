"""
    Código Principal
"""

from src import game

game.jogar(False, (0, 0))
game.jogar(False, (0, 1))
game.jogar(True, (0, 2))

game.jogar(True, (1, 0))
game.jogar(True, (1, 1))
game.jogar(False, (1, 2))

game.jogar(False, (2, 0))
game.jogar(True, (2, 1))
game.jogar(False, (2, 2))

_ = [print(x) for x in game.get_campo()]
print()

acabou = game.game_over()
if acabou[0]:
    resultado = "Empate" if acabou[1] == "" else f'{acabou[1]} Ganhou'
    print(f'Resultado: {resultado}')
    game.reset()


def hello():
    """
        Say Hello
    """
    print("Hello World!")
    return "Hello World!"
