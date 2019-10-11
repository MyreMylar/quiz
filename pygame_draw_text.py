import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))

background = pygame.Surface(screen.get_size())
background = background.convert(screen)
background.fill((220, 220, 220))

font = pygame.font.Font(None, 20)

active_text_string = "A Question?"
my_text_render = font.render(active_text_string, True, pygame.Color("#000000"))
my_text_render_rect = my_text_render.get_rect(centerx=320, centery=240)

new_key_pressed = False
new_key = ""

clock = pygame.time.Clock()
is_running = True
while is_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False
        if event.type == KEYDOWN:
            new_key_pressed = True
            if event.key == K_a:
                new_key = "a"

    if new_key_pressed:
        active_text_string += new_key
        new_key_pressed = False
        new_key = ""

    screen.blit(background, (0, 0))

    screen.blit(my_text_render, my_text_render_rect)

    pygame.display.flip()  # flip all our drawn stuff onto the screen

pygame.quit()  # exited game loop so quit pygame
