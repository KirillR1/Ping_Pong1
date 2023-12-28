from pygame import *



window = display.set_mode((700, 500))
display.set_caption("PingPong")
background = transform.scale(image.load("black.jpg"), (700, 500))


class GameSprite(sprite.Sprite):
        def __init__(self, sprt_image, sprt_x, sprt_y, sprt_speed, width, height, key_up, key_down):
            super().__init__()
            self.image = transform.scale(image.load(sprt_image), (width, height))
            self.rect = self.image.get_rect()
            self.rect.x = sprt_x
            self.rect.y = sprt_y
            self.speed = sprt_speed
            self.key_up = key_up
            self.key_down = key_down
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[self.key_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[self.key_down] and self.rect.y < 420:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        #self.rect.y += self.speed
        pass


player1 = Player("raketka.png", 68, 227, 5, 30, 80, K_w, K_s)
player2 = Player("raketka.png", 600, 227, 5, 30, 80, K_UP, K_DOWN)
ball = Ball("ball.png", 350, 250, 5, 40, 40, K_h, K_y)


clock = time.Clock()
FPS = 60
run = True
finish = False

while run:
    for e in event.get():
            if e.type == QUIT:
                run = False

    if finish != True:
            window.blit(background, (0, 0))
            player1.update()
            player1.reset()
            player2.update()
            player2.reset()
            ball.reset()

    display.update()
    clock.tick(FPS)