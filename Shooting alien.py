import pgzrun
import random
TITLE="Shooting game"
WIDTH=600
HEIGHT=600
message=""
alien=Actor("alien")
def draw():
    screen.clear()
    screen.fill("green")
    alien.draw()
    screen.draw.text(message,center=(300,10))

def placealien():
    alien.x=random.randint(50,WIDTH -50)
    alien.y=random.randint(50,WIDTH -50)
def on_mouse_down(pos):
    global message 
    if alien.collidepoint(pos):
        message="Good shot!"
        placealien()
    else:
        message="Better luck next time!"

    

    
    





placealien()
pgzrun.go()