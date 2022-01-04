import pygame
from pygame.locals import *
from Paddle import *

class Ball():
    def __init__(self, player : Paddle):
        self.reset(player)


    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def reset(self, player):
        self.rad = 10
        if player.x < 300:
            self.x = player.x + player.width
        else:
            self.x = player.x - player.width
        self.y = player.y + player.height/2 - self.rad
        self.rect = Rect(self.x, self.y, self.rad*2, self.rad*2)
        self.speed_x = 4
        self.speed_y = -4