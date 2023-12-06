#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Código para o jogo da velha
    Funções:
    - reset: reinicia o campo de jogo
    - jogar: realiza uma jogada
    - get_campo: retorna o estado atual do campo
    - game_over: verificar se o jogo já acabou
"""
# pylint: disable=global-statement

# Declaração de variáveis
_campo = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1],
]  # -1 == Vazio, 'O', 'X'


def reset():
    """
    Função para reiniciar o jogo

    -1 = Vazio
     0 = O
     1 = X
    """
    global _campo

    _campo = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1],
    ]
    return _campo

def jogar(jogador, posicao):
    """
    Função para realizar jogada no 'Campo'

    Parâmetros:
    Jogador: True = 'O', False = 'X'
    Posição: Onde deve ser realizada a jogada

    Retorna:
    Boolean: Se teve erro durante a execução da jogada

    Erros:
    TypeError: entradas com tipos errados
    ValueError: entrada com valores inválidos
    PermissionError: Posição da jogada já ocupada
    """
    global _campo

    if _campo[posicao[0]][posicao[1]] == -1:
        _campo[posicao[0]][posicao[1]] = 0 if jogador else 1
        return False
    return True

def get_campo():
    """
    Função para recuperar o campo atual.

    Retorna:
    Matrix[3,3]: O Campo de jogo atual.
    """
    return _campo


def game_over():
    """
    Função para verificar o final do jogo e retornar o ganhador

    Retorna:
    Tupla: Fim de jogo, Ganhador
    """
    # Verificação
    for i in range(3):
        # Horizontal
        if (
            _campo[i][0] == _campo[i][1]
            and _campo[i][1] == _campo[i][2]
            and _campo[i][0] != -1
        ):
            return (True, _campo[i][0])  # Alguém Ganhou

        # Horizontal
        if (
            _campo[0][i] == _campo[1][i]
            and _campo[1][i] == _campo[2][i]
            and _campo[0][i] != -1
        ):
            return (True, _campo[0][i])  # Alguém Ganhou

    # Diagonais
    if _campo[0][0] == _campo[1][1] and _campo[1][1] == _campo[2][2]:
        if _campo[0][0] == 0:
            return (True, 0)  # O Ganhou
        if _campo[0][0] == 1:
            return (True, 1)  # X Ganhou

    if _campo[0][2] == _campo[1][1] and _campo[1][1] == _campo[2][0]:
        if _campo[0][2] == 0:
            return (True, 0)  # O Ganhou
        if _campo[0][2] == 1:
            return (True, 1)  # X Ganhou

    cont = 0
    for i in range(3):
        for j in range(3):
            if _campo[i][j] == -1:
                cont += 1
    if cont == 0:
        return (True, -1)  # Empate

    return (False, -1)  # Ainda não acabou
