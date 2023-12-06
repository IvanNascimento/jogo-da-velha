def _config():
    fill(255)
    textSize(40)
    textAlign(CENTER, CENTER)

def welcome():
    _config()
    background(112,112,112)
    text("Jogo da Velha",width/2, height*0.25)
    text("Iniciar como O", width/2, height*0.5)
    text("Iniciar como X", width/2, height*0.6)

def iniciar():
    if mouseX > 195 and mouseX < 305:
        if mouseY > 325 and mouseY < 370:
            return True, True
        if mouseY > 400 and mouseY < 440:
            return True, False 
    return False, False
