from random import randint
from pygame import *
lost = 0
window = display.set_mode((700, 500))
display.set_caption('Шутер')
clock = time.Clock()
background = transform.scale(image.load('fon.jpg'), (700, 500))

circle_top = None
circle_right = None

win_height = 500
win_width = 700

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
        self.rect.x += self.speed
        if self.rect.x >= 650:
            global circle_right
            circle_right = True
        if self.rect.y <= 5:
            global circle_top
            circle_top = True
        else:
            circle_top = False
        if self.rect.y > 450:
            self.rect.y -= self.speed
        if circle_right:
            self.rect.x -= self.speed
        else: 
            self.rect.y -= self.speed
        if circle_top:
            self.rect.y -= self.speed
        else: 
            self.rect.y += self.speed

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
        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        display.update()