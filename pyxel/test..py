import pyxel

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
        

def draw():
    pyxel.cls(0)
    pyxel.text(0, 0, "marcos imbecil", 2)
    pyxel.text(0, 10, "marcos puto maricon", pyxel.frame_count % 16)
    pyxel.line(0, 0, 20, 20, 3)
    pyxel.rect(20, 20, 10, 30, 4)
    pyxel.rectb(30, 50, 20, 10, 5)
    pyxel.circ(50, 80, 10, 6)
    pyxel.circb(100, 30, 15, 7)
    pyxel.pset(120, 100, 8)

WIDTH = 256
HEIGHT = 256
cap = "xd"
pyxel.init(WIDTH, HEIGHT, title = cap)
pyxel.run(update, draw)
