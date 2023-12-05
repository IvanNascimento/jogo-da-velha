"""
    Interface de linha de comando para o Jogo da Velha
"""
# pylint: disable=global-statement, invalid-name
import sys, os

this_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_dir, "../src"))
sys.path.append(os.path.join(this_dir, "../ai"))

import game
import move

# Variáveis
_jogador = None
_pontuacao = (0, 0)
_count = 0
_partidas = 0
_posicoes = ["1", "2", "3", "a", "b", "c", "A", "B", "C"]
_numeros = ["1", "2", "3"]
_letras = ["a", "b", "c", "A", "B", "C"]
_ganhador = ""
_maquina = False


def _init():
    """
    Pega os valores iniciais do jogo
    """
    global _jogador, _maquina
    print("Jogar contra o computador ?")
    print("s - Sim")
    print("n - Não")
    res = input()
    # Valida a entrada
    if res not in ["s", "S", "n", "N", "y", "Y"]:
        print("Opção válida. Escolha corretamente")
        return _init()

    print("Quem jogara primeiro ?")
    print("1: x xis")
    print("2: O circulo")
    res2 = input()
    # Valida a entrada
    if res2 not in ["1", "2", "x", "o", "X", "O", "0"]:
        print("Opção válida. Escolha corretamente")
        return _init()

    _maquina = res in ["s", "S", "y", "Y"]
    _jogador = res2 in ["2", "o", "O", "0"]
    print(f'{"O" if _jogador else "X"} começa o jogo')


def print_campo():
    """
    Função para mostrar o campo de maneira legível

    Retorno:
    None
    """
    game_campo = list(game.get_campo())
    campo = []
    for i in range(3):
        add = []
        for j in range(3):
            if game_campo[i][j] == 0:
                add.append("O")
            elif game_campo[i][j] == 1:
                add.append("X")
            else:
                add.append(" ")
        campo.append(add)

    print("    A   B   C  ")
    print("  ┌───┬───┬───┐")
    print(f"1 │ {campo[0][0]} │ {campo[0][1]} │ {campo[0][2]} │")
    print("  ├───┼───┼───┤")
    print(f"2 │ {campo[1][0]} │ {campo[1][1]} │ {campo[1][2]} │")
    print("  ├───┼───┼───┤")
    print(f"3 │ {campo[2][0]} │ {campo[2][1]} │ {campo[2][2]} │")
    print("  └───┴───┴───┘")


def _jogar():
    """
    Função para executar a jogada

    Retorno:
    - bool: jogada inválida
    """
    global _jogador, _count
    print_campo()

    print(f"Jogador {1 if _count %2 == 0 else 2}, Qual sua jogada ? ex.: A 1 ou 1 A ")
    _ignore = False
    _invalido = False

    if _count % 2 != 0 and _maquina:
        campo = game.get_campo()
        posicao = move.play(campo)
        _ignore = True
    else:
        casa = input()
        posicao = casa.split()
        _ignore = False

    if not _ignore:
        if posicao[0] not in _posicoes or posicao[1] not in _posicoes:
            _invalido = True
        elif posicao[0] in _numeros and posicao[1] in _numeros:
            _invalido = True
        elif posicao[0] in _letras and posicao[1] in _letras:
            _invalido = True

        if _invalido:
            print("Posição inválida.")
            return True

        if posicao[1] in _letras:
            posicao = [posicao[1], int(posicao[0])]
        else:
            posicao = [posicao[0], int(posicao[1])]

        match (posicao[0].lower()):
            case "a":
                posicao = (posicao[1] - 1, 0)
            case "b":
                posicao = (posicao[1] - 1, 1)
            case _:
                posicao = (posicao[1] - 1, 2)

    try:
        game.jogar(_jogador, posicao)
    except ValueError:
        print("Informe um valor aceitável")
        return True
    except PermissionError:
        print("Deve jogar em uma casa livre")
        return True

    _jogador = not _jogador
    _count += 1
    return False


def _game_over():
    print_campo()
    print("Fim de jogo")
    print(f"Ganhador: {'Empate' if _ganhador == -1 else _ganhador}")
    print(f"Número de partidas: {_partidas}")
    print(f"Pontuação 1° Jogador: {_pontuacao[0]}")
    print(f"Pontuação 2° Jogador: {_pontuacao[1]}")
    game.reset()


def _loop():
    global _pontuacao, _partidas, _ganhador
    while True:
        _jogar()
        temp = game.game_over()
        if temp[0]:
            _ganhador = "O" if temp[1] == 0 else "X" if temp[1] == 1 else "Empate"
            if temp[1] == -1:
                _pontuacao = (_pontuacao[0] + 1, _pontuacao[1] + 1)
            else:
                if _count % 2 == 0:
                    _pontuacao = (_pontuacao[0], _pontuacao[1] + 1)
                else:
                    _pontuacao = (_pontuacao[0] + 1, _pontuacao[1])
            _partidas += 1
            break
    _game_over()
    print("Jogar novamente? 1 - Sim, 2 - Não")
    res = input()
    # print(f"Resposta: {res}")
    if res in ["1", "s", "sim", "Sim", "S", "y", "Y", "yes", "Yes"]:
        main()
    else:
        print("Até a próxima")


def main():
    """
    Função principal
    """
    _init()
    _loop()
