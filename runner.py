import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))    # (w,h)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(
    'font/Pixeltype.ttf', 50)  # (font type, font size)


sky_surface = pygame.image.load('graphics/sky.png')  # (w,h)
ground_surface = pygame.image.load('graphics/ground.png')

# (text, anti aliasing, color)
text_surface = test_font.render('My game', False, 'Black')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))   # (from left, from top-down )
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)
