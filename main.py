import pgzrun

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.VelocityX = 2
        self.VelocityY = 2

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, (255, 255, 255))

    def update(self):
        self.x += self.VelocityX
        self.y += self.VelocityY

        if self.x > WIDTH or self.x < 0:
            self.VelocityX = -self.VelocityX
        if self.y > HEIGHT or self.y < 0:
            self.VelocityY = -self.VelocityY


def draw():
    pass
   

def update(dt):
    pass


pgzrun.go()