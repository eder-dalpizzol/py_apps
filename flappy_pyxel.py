import random
import pyxel

class FlappyBird:
    def __init__(self):
        pyxel.init(160, 120)
        self.bird_x = 40
        self.bird_y = 60
        self.bird_vy = 0
        self.gravity = 0.3
        self.pipe_x = 150
        self.pipe_y = random.randint(20,100)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bird_vy = -5
        
        self.bird_vy += self.gravity
        self.bird_y += self.bird_vy
        self.pipe_x -= 1

        if (self.bird_y > 120 or self.bird_y < 0 or
                (self.bird_x + 4 > self.pipe_x and self.bird_x < self.pipe_x + 6) and
                (self.bird_y < self.pipe_y or self.bird_y + 4 > self.pipe_y + 20)):
            pyxel.quit()
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.pipe_x, self.pipe_y, 6, 20, 7)
        pyxel.rect(self.pipe_x, self.pipe_y + 20, 6, 100, 7)
        pyxel.rect(self.bird_x, self.bird_y, 4, 4, 1)

FlappyBird()
