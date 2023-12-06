# -*- coding: utf-8 -*-

def _config():
    fill(255)
    textSize(25)
    textAlign(CENTER, CENTER)


def game_over(pontos):
    _config()
    background(112,112,112)
    text("Tela de Game Over", width/2, height*0.3)
    text("Jogar novamente?", width/2, height*0.4)
    text("Sim", 200, height*0.5)
    text("Nao", 300, height*0.5)
    
    textAlign(CENTER, CENTER)
    text("Pontuacao", 250, 400)
    text("Jogador 1:", 175, 440)
    text("Jogador 2:", 175, 470)
    text(pontos[0], 275, 440)
    text(pontos[1], 275, 470)

def replay():
    if mouseX > 175 and mouseX < 225:
        if mouseY > 330 and mouseY < 360:
            return True
    if mouseX > 265 and mouseX < 325:
        if mouseY > 330 and mouseY < 360:
            return False
    return -1
