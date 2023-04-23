from random import randint
from pygame import *
win_height = 500
win_width = 700
lost = 0
window = display.set_mode((700, 500))
display.set_caption('Шутер')
clock = time.Clock()
background = transform.scale(image.load('fon.jpg'), (win_width, win_height))

speed_x = 1 # скорость по x
speed_y = 1 # скорость по y




#font
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_RIGHT] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y
player1 = Player1('player1.png', 5, win_height -80, 4, 80, 1 )
player2 = Player2('player2.png', 635, win_height -85, 4, 80, 1 )
ball = Ball('ball.png', 100, 100, 10, 10, 1)
game = True
finish = False
FPS = 60
while game:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if ball.rect.y > win_height:
            speed_y *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        display.update()