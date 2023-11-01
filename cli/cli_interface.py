"""
    Interface de linha de comando para o Jogo da Velha
"""
# pylint: disable=global-statement

from src import game

# Variáveis
_jogador = None
_pontuacao = (0, 0)
_count = 0
_partidas = 0


def _init():
    """
    Pega os valores iniciais do jogo
    """
    print('Quem jogara primeiro ?')
    print('1: O circulo')
    print('2: X xis')
    res = int(input())
    global _jogador
    _jogador = res == 1
    print(f'{"O" if _jogador else "X"} começa o jogo')


def print_campo():
    """
    Função para mostrar o campo de maneira legivel

    Retorno:
    None
    """
    campo = game.get_campo()
    to_print = [[
        campo[0][0] if campo[0][0] != -1 else " ",
        campo[0][1] if campo[0][1] != -1 else " ",
        campo[0][2] if campo[0][2] != -1 else " "
    ], [
        campo[1][0] if campo[1][0] != -1 else " ",
        campo[1][1] if campo[1][1] != -1 else " ",
        campo[1][2] if campo[1][2] != -1 else " "
    ], [
        campo[2][0] if campo[2][0] != -1 else " ",
        campo[2][1] if campo[2][1] != -1 else " ",
        campo[2][2] if campo[2][2] != -1 else " ",
        campo[2][2] if campo[2][2] != -1 else " "
    ]]
    print('  -A-|-B-|-C- ')
    print(f' 1 {to_print[0][0]} | {to_print[0][1]} | {to_print[0][2]} ')
    print(' |---|---|---')
    print(f' 2 {to_print[1][0]} | {to_print[1][1]} | {to_print[1][2]} ')
    print(' |---|---|---')
    print(f' 3 {to_print[2][0]} | {to_print[2][1]} | {to_print[2][2]} ')


def _jogar():
    """
    Função para executar a jogada

    Retorno: 
    - bool: jogada inválida
    """
    global _jogador, _count
    print_campo()
    if _count % 2 == 0:
        print('Jogador 1, ', end="")
    else:
        print('Jogador 2, ', end="")
    casa = input('Qual sua jogada ? ex.: 1 A \n')
    posicao = casa.split()
    try:
        int(posicao[0])
    except ValueError:
        print('Posição inválida')
        return True
    if int(posicao[0]) < 1 or int(posicao[0]) > 3:
        print('Posição inválida')
        return True
    match (posicao[1].lower()):
        case 'a':
            posicao = (int(posicao[0]) - 1, 0)
        case 'b':
            posicao = (int(posicao[0]) - 1, 1)
        case _:
            posicao = (int(posicao[0]) - 1, 2)
    try:
        game.jogar(_jogador, posicao)
    except ValueError:
        print('Informe um valor aceitavel')
        return True
    except PermissionError:
        print('Deve jogar em uma casa livre')
        return True

    _jogador = not _jogador
    _count += 1
    return False


def _game_over():
    global _count
    print("Fim de jogo")
    print(f'Número de partidas: {_partidas}')
    print(f'Pontuação 1° Jogador: {_pontuacao[0]}')
    print(f'Pontuação 2° Jogador: {_pontuacao[1]}')
    game.reset()


def _loop():
    global _pontuacao, _partidas
    while True:
        _jogar()
        temp = game.game_over()
        if temp[0]:
            if temp[1] == "":
                _pontuacao = (_pontuacao[0] + 1, _pontuacao[1] + 1)
            else:
                if _count % 2 == 0:
                    _pontuacao = (_pontuacao[0], _pontuacao[1] + 1)
                else:
                    _pontuacao = (_pontuacao[0] + 1, _pontuacao[1])
            _partidas += 1
            break
    _game_over()
    print('Jogar novamente? 1 - Sim, 2 - Não')
    res = int(input())
    if res == 1:
        main()


def main():
    """
    Função principal
    """
    _init()
    _loop()


if __name__ == "main":
    main()
