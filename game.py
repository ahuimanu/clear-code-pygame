import pygame
from sys import exit

from snail import Snail
from player import Player
from gutils import degrees_to_radians

# constants
WIDTH, HEIGHT = 800, 400
gravity = 0


def display_score():
    current_time = pygame.time.get_ticks()
    score_surf = test_font.render(
        f"Score: {current_time // 1000}", True, text_color_main
    )
    score_rect = score_surf.get_rect(midright=(WIDTH - 50, 50))
    screen.blit(score_surf, score_rect)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Dude Abides")

# game variables
clock = pygame.time.Clock()
test_font = pygame.font.Font("assets/Pixeltype.ttf", 50)
text_color_main = pygame.Color("black")

game_states = ["running", "paused", "over"]
game_state = game_states[0]

# objects
deg = degrees_to_radians(1)
snail = Snail((deg, -1.5))
snail.rect.bottomright = (WIDTH, HEIGHT * 0.75)

player = Player((0, 0))
player.rect.bottomleft = (WIDTH * 0.02, HEIGHT * 0.75)

# surfaces
sky_surface = pygame.image.load("assets/sky.png").convert()
ground_surface = pygame.image.load("assets/ground.png").convert()

# event loop
while True:
    # detect events ############################################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_state == "running":
            if event.type == pygame.MOUSEBUTTONDOWN:
                snail.is_mouse_pressed()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.rect.bottom == 300:
                    gravity = -12
                    print("Spacebar pressed")

                if event.key == pygame.K_RIGHT:
                    player.vector = (0, 2)
                    print("Right arrow pressed")

                if event.key == pygame.K_LEFT:
                    player.vector = (0, -2)
                    print("Left arrow pressed")

                if event.key == pygame.K_p:
                    if game_state == game_states[1]:
                        game_state = game_states[0]
                        print("Game unpaused")
                    else:
                        game_state = game_states[1]
                        print("Game paused")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    print("Spacebar released")

                if event.key == pygame.K_RIGHT:
                    player.vector = (0, 0)

                if event.key == pygame.K_LEFT:
                    player.vector = (0, 0)
        
        if game_state == "over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_restart_rect.collidepoint(event.pos):
                    game_state = game_states[0]
                    snail.rect.bottomright = (WIDTH, HEIGHT * 0.75)
                    player.rect.bottomleft = (WIDTH * 0.02, HEIGHT * 0.75)
                    gravity = 0

        if game_state == "paused":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if game_state == game_states[1]:
                        game_state = game_states[0]
                        print("Game unpaused")
                    else:
                        game_state = game_states[1]
                        print("Game paused")

    # update game ##############################################################
    if game_state == "over":
        screen.fill("deepskyblue2")
        text_game_over_surf = test_font.render("Game Over", True, text_color_main)
        text_game_over_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(text_game_over_surf, text_game_over_rect)

        text_restart_surf = test_font.render("Restart", True, text_color_main)
        text_restart_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT * .66))
        screen.blit(text_restart_surf, text_restart_rect)

    if game_state == "paused":
        screen.fill("deepskyblue3")
        text_surf = test_font.render("Paused", True, text_color_main)
        text_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))        
        screen.blit(text_surf, text_rect)        

    if game_state == "running":
        # draw elements
        screen.fill((255, 255, 255))
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        display_score()

        # pygame.draw.rect(screen, "Pink", text_rect, width=5, border_radius=20)
        # pygame.draw.line(screen, "Blue", (0, 0), (WIDTH, HEIGHT), width=5)
        text_surf = test_font.render("The Dude", True, text_color_main)
        text_rect = text_surf.get_rect(center=(WIDTH / 2, 50))
        screen.blit(text_surf, text_rect)

        snail.update(window=screen)
        screen.blit(snail.image, snail.rect)
        game_state = snail.collide(player)

        snail.is_mouse_over()

        # player
        gravity += 0.5
        player.rect.y += gravity
        player.update()
        screen.blit(player.image, player.rect)


    # render game ##############################################################
    # pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  # 60 fps
