import pygame

class Samsung(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("tom.jpg")
        self.image2 = pygame.image.load("singe.jpg")
        self.image = pygame.transform.scale(self.image, (454, 606))
        self.image2 = pygame.transform.scale(self.image2, (454, 606))
        self.rect = self.image.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect.x = 200
        self.rect2.x = x
        self.rect2.y = y
        self.rect.y = 600
        self.speed = 4
        self.speed2 = 2

    def move_right(self):
        self.rect.x += self.speed
    
    def move_right1(self):
        self.rect2.x += self.speed2

    def move_left(self):
        self.rect.x -= self.speed
        
    def move_left1(self):
        self.rect2.x -= self.speed2

    def move_up(self):
        self.rect.y -= self.speed

    def move_up1(self):
        self.rect2.y -= self.speed2

    def move_down(self):
        self.rect.y += self.speed

    def move_down1(self):
        self.rect2.y += self.speed2
