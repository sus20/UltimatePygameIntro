import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))    # (w,h)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(
    'font/Pixeltype.ttf', 50)  # (font type, font size)


sky_surface = pygame.image.load('graphics/sky.png').convert()  # (w,h)
ground_surface = pygame.image.load('graphics/ground.png').convert()


# (text, antiAliasing, color)
score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(bottomright=(400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(bottomright=(80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))   # (from left, from top-down )
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
