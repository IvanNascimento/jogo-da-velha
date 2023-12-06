_posicoes = [[(150,150), (250,150), (350,150)],
             [(150,250), (250,250), (350,250)],
             [(150,350), (250,350), (350,350)]]

def _config():
    fill(255)
    textAlign(CENTER, CENTER)
    stroke(0)
    strokeWeight(4)

def jogo(campo, pontos, jogador):
    _config()
    background(112,112,112)
    # Campo
    line(200,100,200,400)
    line(300,100,300,400)
    line(100,200,400,200)
    line(100,300,400,300)
    # Jogadas
    textSize(75)
    for i in range(3):
        for j in range(3):
            if campo[i][j] == 0:
                p = _posicoes[i][j]
                fill(0,0,200)
                text("O", p[0], p[1])
            elif campo[i][j] == 1:
                p = _posicoes[i][j]
                fill(200,0,0)
                text("X", p[0],p[1])
    # Placar
    fill(255)
    line(0,500,500,500)
    noStroke()
    rect(0,500,500,200)
    stroke(0)
    textSize(30)
    fill(0)
    text("Placar", 250, 525)
    text("Jogador 1: ", 80, 580)
    text("Jogador 2: ", 80, 620)
    textAlign(LEFT, CENTER)
    text(pontos[0], 150, 580)
    text(pontos[1], 150, 620)
    
    # Jogador da vez
    textAlign(CENTER,  CENTER)
    fill(0)
    text("Vez do", 370, 540)
    fill(112)
    rect(320, 560, 100, 100)
    stroke(0)
    if jogador:
        fill(0,0,200)
    else:
        fill(200,0,0)
    textSize(75)
    text("O" if jogador else "X", 370, 610)

            
def jogada():
    if mouseX > 100 and mouseX < 200:
        if mouseY > 100 and mouseY < 200:
            return (0,0)
        if mouseY > 200 and mouseY < 300:
            return (1,0)
        if mouseY > 300 and mouseY < 400:
            return (2,0)
    if mouseX > 200 and mouseX < 300:
        if mouseY > 100 and mouseY < 200:
            return (0,1)
        if mouseY > 200 and mouseY < 300:
            return (1,1)
        if mouseY > 300 and mouseY < 400:
            return (2,1)
    if mouseX > 300 and mouseX < 400:
        if mouseY > 100 and mouseY < 200:
            return (0,2)
        if mouseY > 200 and mouseY < 300:
            return (1,2)
        if mouseY > 300 and mouseY < 400:
            return (2,2)
    return (-1, -1)
