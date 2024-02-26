from typing import Any
import pygame
import math


class Snail(pygame.sprite.Sprite):
    """A snail that will move across the screen
    Returns: snail object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/snail1.png").convert_alpha()
        # https://pyga.me/docs/ref/surface.html#pygame.Surface.get_frect
        self.rect = self.image.get_frect()
        self.vector = vector

    def calcnewpos(self, rect) -> pygame.Rect:
        (angle, z) = self.vector
        (dx, dy) = (z * math.cos(angle), z * math.sin(angle))
        return rect.move(dx, dy)

    def collide(self, player):
        if self.rect.colliderect(player.rect):
            print("snail collided with player")
            state = "over"
            return state
        else:
            return "running"

    def is_mouse_over(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            print(
                f"da mouse hovers over snail at {mouse_pos} and snail rect is {self.rect}"
            )

    def is_mouse_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                print(
                    f"da mouse click da snail at {mouse_pos} and snail rect is {self.rect}"
                )

    def update(self, window):
        newpos = self.calcnewpos(self.rect)
        if self.rect.left < 0:
            self.rect.left = 0
            self.vector = (self.vector[0], self.vector[1] * -1)
            newpos = self.calcnewpos(self.rect)
        elif self.rect.right > window.get_width():
            self.rect.right = window.get_width() - 1
            self.vector = (self.vector[0], self.vector[1] * -1)
            newpos = self.calcnewpos(self.rect)
        elif self.rect.top < 0:
            self.rect.top = 0
            self.vector = (self.vector[0], self.vector[1] * -1)
            newpos = self.calcnewpos(self.rect)
        elif self.rect.bottom > window.get_height():
            self.rect.bottom = window.get_height() - 1
            self.vector = (self.vector[0], self.vector[1] * -1)
            newpos = self.calcnewpos(self.rect)
        else:
            self.rect = newpos
