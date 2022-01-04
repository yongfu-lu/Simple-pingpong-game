import pygame
from pygame.locals import *

class Paddle():
    def __init__(self, player, screen_width, screen_height):
        self.reset(player, screen_width, screen_height)

    def move(self, direction):
        if(direction == 1):
            self.y += self.speed
            self.rect.y += self.speed
        else:
            self.y -= self.speed
            self.rect.y -= self.speed


    def reset(self, player, screen_width, screen_height):
        self.height = 80
        self.width = 20
        if (player == 1):
            self.x = 20
        else:
            self.x = screen_width - 40
        self.y = screen_height / 2 - self.height / 2

        self.speed = 15
        self.rect = Rect(self.x, self.y, self.width, self.height)


