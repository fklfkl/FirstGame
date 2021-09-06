import pyxel
import math

circleRadius = 10
textX = 20
textY = 50

def main():
    pyxel.init(256,256, caption="My First Game", scale=3)
    pyxel.run(update, draw)

def update():
    global circleRadius
    circleRadius = 10 + 20 * math.sin(pyxel.frame_count / 4)
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(5)
    for i in range(10):
        pyxel.text(textX,textY+5*i,"Hello",((pyxel.frame_count + i) / 4) % 16)
    pyxel.circ(128,128,circleRadius,4)
    pass

main()
