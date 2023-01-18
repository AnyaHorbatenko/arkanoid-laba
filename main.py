import pgzrun

WIDTH = 800
HEIGHT = 600

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect((self.x, self. y), (self.width, self.height))

    def draw(self):
        screen.draw.filled_rect(Rect((self.x, self.y), (self.width, self.height)), (255, 255, 255))

    def update(self):
        self.x = pg.mouse.get_pos()[0]
        if self.x < -100:
            self.x = 0
        if self.x > WIDTH-50:
            self.x = WIDTH-100
        
    def check_collision(self, ball):
        if ball.x > self.x and ball.x < self.x + self.width and ball.y > self.y and ball.y < self.y + self.height:
            ball.VelocityY = -ball.VelocityY

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

ball = Ball(400, 300, 10)
paddle = Paddle(120, 550, 100, 100)

def draw():
    screen.clear()
    screen.fill((123, 221, 65))
    screen.draw.text("Score: " + str(score), (500, 500), color=(0, 0, 0), background="white")
    ball.draw()
    paddle.draw()
   

def update(dt):
    ball.update()
    paddle.update()


pgzrun.go()