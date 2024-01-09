from pygame import *
import os

font.init()
win_height = 700
win_width = 500
window = display.set_mode((win_height, win_width))
display.set_caption("PingPong")
#background = transform.scale(image.load("ball.png"), (win_height, win_width))
window.fill((0, 0, 0))
font2 = font.SysFont('Arial', 50)

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
        #self.rect.x += self.speed
        pass

current_path = os.path.dirname(__file__)
    


player1 = Player(os.path.join(current_path, 'raketka.png'), 68, 227, 5, 30, 80, K_w, K_s)
player2 = Player(os.path.join(current_path, 'raketka.png'), 600, 227, 5, 30, 80, K_UP, K_DOWN)
ball = Ball(os.path.join(current_path, 'ball.png'), 300, 250, 5, 40, 40, K_h, K_y)

txt_WIN1 = font2.render("PLAYER 1 WIN", 1, (0, 255, 0))
txt_LOSE1 = font2.render("PLAYER 1 LOSE", 1, (255, 0, 0))
txt_WIN2 = font2.render("PLAYER 2 WIN", 1, (0, 255, 0))
txt_LOSE2 = font2.render("PLAYER 2 LOSE", 1, (255, 0, 0))

b_speed_x = 4
b_speed_y = 4
clock = time.Clock()
FPS = 60
run = True
finish = False

while run:
    for e in event.get():
            if e.type == QUIT:
                run = False

    if finish != True:
            window.fill((0, 0, 0))
            player1.update()
            player1.reset()
            player2.update()
            player2.reset()
            ball.reset()
            ball.rect.x += b_speed_x
            ball.rect.y += b_speed_y
            if ball.rect.y > win_width-50 or ball.rect.y < 0:
                b_speed_y *= -1
            if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
                b_speed_x *= -1
            if ball.rect.x > win_height-40: #or ball.rect.x < 0:
                window.blit(txt_LOSE2, (205, 270))
                window.blit(txt_WIN1, (220, 190))
                finish = True
            if ball.rect.x < 0:
                window.blit(txt_LOSE1, (205, 270))
                window.blit(txt_WIN2, (220, 190))
                finish = True


    display.update()
    clock.tick(FPS)