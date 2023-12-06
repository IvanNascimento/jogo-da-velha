from welcome import *
from interface import *
from game_over import *

import game
import move


# 1 - welcome, 2 - jogo, 3 - game over
tela = 1

_pontos = [0,0]
_jogador = False
campo_atual = game.get_campo()


def setup():
    size(500, 700)

def devHelper():
    textSize(15)
    fill(0)
    stroke(0)
    strokeWeight(1)
    textAlign(CENTER, CENTER)
    X = mouseX if mouseX else 0
    Y = mouseY if mouseY else 0
    string = "X: {}\n Y: {}".format(X, Y)
    text(string, X + 20, Y - 20)
    line(X, 0, X, height)
    line(0, Y, width, Y)
    

# loop
def draw():
    if tela == 1:
        welcome()
    elif tela == 2:
        jogo(campo_atual, _pontos, _jogador)
    else:
        game_over(_pontos)
    devHelper()


def verificar():
    global tela
    fim = game.game_over()
    if fim[0]:
        if fim[1] == 0:
            _pontos[1] += 1
        elif fim[1] == 1:
            _pontos[0] += 1
        else:
            _pontos[0] += 1
            _pontos[1] += 1
        tela = 3

def mouseClicked():
    global tela, _jogador, campo_atual
    if tela == 1:
        resultado = iniciar()
        if resultado[0]:
            tela = 2
            _jogador = resultado[1]
    elif tela == 2:
        resultado = jogada()
        if resultado != (-1,-1):
            falhou = game.jogar(_jogador, resultado)
            verificar()
            if not falhou and tela == 2:
                _jogador = not _jogador
                maquina = move.play(campo_atual)
                game.jogar(_jogador, maquina)
                _jogador = not _jogador
                verificar()
    elif tela == 3:
        novamente = replay()
        if novamente == True:
            campo_atual = game.reset()
            tela = 1
        if novamente == False:
            exit()
            return
