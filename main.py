import pygame
from mov import Samsung
pygame.init()

# Important
WIDTH = 2000
HEIGHT = 1500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Variables
samsung = Samsung(0, 0)
up = False
up1 = False
down = False
down1 = False
right = False
right1 = False
left = False
left1 = False
clock = pygame.time.Clock()

down = True
down1 = True
right = True
right1 = True

'''Boucle jeu'''
running = True
while running:

    '''Evenements'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    '''Affichage'''
    screen.blit(screen, (0, 0))
    screen.fill([255, 255, 255])
    screen.blit(background, (0, 0))
    screen.blit(samsung.image, samsung.rect)
    screen.blit(samsung.image2, samsung.rect2)
    pygame.display.flip()

    # Lucas width = 160
    # Lucas height = 190

    # Singe width = 1280
    # Singe height = 959

    '''Déplacement'''
    # BAS
    if samsung.rect.y >= HEIGHT - 606:
        down = False
        up = True
    if samsung.rect2.y >= HEIGHT - 606:
        down1 = False
        up1 = True

    # DROITE
    if samsung.rect.x >= WIDTH - 454:
        right = False
        left = True
    if samsung.rect2.x >= WIDTH - 454:
        right1 = False
        left1 = True

    # GAUCHE
    if samsung.rect.x <= 0:
        left = False
        right = True
    if samsung.rect2.x <= 0:
        left1 = False
        right1 = True

    # HAUT
    if samsung.rect.y <= 0:
        up = False
        down = True
    if samsung.rect2.y <= 0:
        up1 = False
        down1 = True

    if down == True:
        samsung.move_down()
    if up == True:
        samsung.move_up()
    if right == True:
        samsung.move_right()
    if left == True:
        samsung.move_left()

    if down1 == True:
        samsung.move_down1()
    if up1 == True:
        samsung.move_up1()
    if right1 == True:
        samsung.move_right1()
    if left1 == True:
        samsung.move_left1()

    clock.tick(60)

pygame.quit()