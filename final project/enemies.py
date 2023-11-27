import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.x = (self.x + 1) % pyxel.width
        elif pyxel.btnp(pyxel.KEY_LEFT):
            self.x = (self.x - 1) % pyxel.width
        elif pyxel.btnp(pyxel.KEY_UP):
            self.y = (self.y + 1) % pyxel.height
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self.y = (self.y - 1) % pyxel.height

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()