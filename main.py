from random import randint
from pygame import *
lost = 0
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('fon.jpg'), (700, 500))

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
    pass

player1 = Player1('player1.png', 5, win_height -80, 4, 80, 3 )
player2 = Player2('player2.png', 635, win_height -85, 4, 80, 3 )
game = True
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.reset()
    player1.update()
    player2.reset()
    player2.update()
    display.update()