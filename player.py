from typing import Any
import pygame
import math


class Player(pygame.sprite.Sprite):
    """A player can be moved around the screen
    Returns: snail object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/player_stand.png").convert_alpha()
        # https://pyga.me/docs/ref/surface.html#pygame.Surface.get_frect
        self.rect = self.image.get_frect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect)
        self.rect = newpos

    def calcnewpos(self, rect) -> pygame.Rect:
        (angle, z) = self.vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return rect.move(dx, dy)
