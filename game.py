import pygame
from sys import exit

from snail import Snail
from player import Player
from gutils import degrees_to_radians

# constants
WIDTH, HEIGHT = 800, 400

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Dude Abides")

# game variables
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/Pixeltype.ttf", 50)
text_color_main = pygame.Color("black")

# objects
deg = degrees_to_radians(1)
snail = Snail((deg, -1.5))
snail.rect.bottomright = (WIDTH, HEIGHT * 0.75)

player = Player((0, 0))
player.rect.bottomleft = (WIDTH * 0.02, HEIGHT * 0.75)

# surfaces
sky_surface = pygame.image.load("assets/sky.png").convert()
ground_surface = pygame.image.load("assets/ground.png").convert()
text_surface = test_font.render("The Dude", True, text_color_main)


while True:
    # detect events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw elements
    screen.fill((255, 255, 255))
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    screen.blit(snail.image, snail.rect)
    snail.update(window=screen)

    screen.blit(player.image, player.rect)
    player.update()

    # print(f"angle: {snail.vector[0]}: rect: {snail.rect}")

    # update
    # pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  # 60 fps
