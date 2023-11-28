import pyxel

class App:
    def __init__(self):
        pyxel.init(256, 240, title="Super Mario 1983")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 20, "A ella no le gusta el reggaeton", 8)
        pyxel.text(10, 30, "pero le encanta como canta la sensacion", 12)
App()