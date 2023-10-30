from jogo_da_velha import *

jogar(False, (0, 0))
jogar(False, (0, 1))
jogar(True, (0, 2))

jogar(True, (1, 0))
jogar(True, (1, 1))
jogar(False, (1, 2))

jogar(False, (2, 0))
jogar(True, (2, 1))
jogar(False, (2, 2))

[print(x) for x in getCampo()]

print(gameOver())


def hello():
    print("Hello World!")
    return "Hello World!"
