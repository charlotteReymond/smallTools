
def setup():
    size(500,600)#définit la taille du sketch
    colorMode(HSB)
    background(35)#fond en gris foncé
    noStroke()
def draw():
    for x in range(20,420):
        for y in range(20,420):
            fill(y/1.6,x/2,255)#couleur de la grille
            rect(x,y,1,1)
    textSize(32)
    fill(35)
    rect(20,480,600,100)#effacer linscription
    fill(200)
    coordY=str(round(mouseY/1.6))
    coordX=str(round(mouseX/2))
    fill(round(mouseY/1.6),round(mouseX/2),255) 
    text("HSB: "+coordY+" / "+coordX+" / 255",20,520)
    fill(60)
    textSize(20)
    text("hue    saturation   brightness",100,550)
