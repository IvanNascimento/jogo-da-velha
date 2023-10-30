# Declaração de variáveis
campo = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1],
]  # -1 == Vazio, 'O', 'X'


def reset():
    """
    Função para reiniciar o jogo
    """
    global campo
    campo = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1],
    ]


def jogar(jogador: bool, posicao: tuple[int, int]) -> bool:
    global campo
    """
    Função para realizar jogada no 'Campo'

    Parâmetros:
    Jogador: True = 'O', False = 'X'
    Posição: Onde deve ser realizada a jogada

    Retorna:
    Boolean: Se teve erro durante a execução da jogada
    """

    # Type validation
    if type(jogador) != bool or type(posicao) != tuple:
        raise Exception(
            f"Tipo inválido, Jogador deve ser 'bool' e Posição deve ser 'tuple[int, int]'"
        )
    if type(posicao[0]) != int or type(posicao[1]) != int:
        raise Exception(f"Tipo inválido, Posição deve ser 'tuple[int, int]'")

    # Values validation
    if 0 > posicao[0] or posicao[0] > 2:
        raise ValueError(f"valores de Posição devem estar entre 0 e 2")
    if 0 > posicao[1] or posicao[1] > 2:
        raise ValueError(f"valores de Posição devem estar entre 0 e 2")

    if campo[posicao[0]][posicao[1]] == -1:
        campo[posicao[0]][posicao[1]] = "O" if jogador else "X"
        return False
    else:
        raise Exception(f"Posição já está em uso ")


def getCampo():
    """
    Função para recuperar o campo atual.

    Retorna:
    Matrix[3,3]: O Campo de jogo atual.
    """
    global campo
    return campo


def gameOver() -> tuple[bool, str]:
    """
    Função para verificar o final do jogo e retornar o ganhador

    Retorna:
    Tupla: Fim de jogo, Ganhador
    """
    global campo
    # Verificação
    for i in range(3):
        # Horizontal
        if (
            campo[i][0] == campo[i][1]
            and campo[i][1] == campo[i][2]
            and campo[i][0] != -1
        ):
            return (True, campo[i][0])  # Alguém Ganhou
        # Horizontal
        if (
            campo[0][i] == campo[1][i]
            and campo[1][i] == campo[2][i]
            and campo[0][i] != -1
        ):
            return (True, campo[0][i])  # Alguém Ganhou

    # Diagonais
    if campo[0][0] == campo[1][1] and campo[1][1] == campo[2][2]:
        if campo[0][0] == "O":
            return (True, "O")  # O Ganhou
        if campo[0][0] == "X":
            return (True, "X")  # X Ganhou

    if campo[0][2] == campo[1][1] and campo[1][1] == campo[2][0]:
        if campo[0][2] == "O":
            return (True, "O")  # O Ganhou
        if campo[0][2] == "X":
            return (True, "X")  # X Ganhou

    cont = 0
    for i in range(3):
        for j in range(3):
            if campo[i][j] == -1:
                cont += 1
    if cont == 0:
        return (True, "")  # Empate
    else:
        return (False, "")  # Ainda não acabou
