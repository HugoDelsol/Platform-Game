import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.speed = 0.2
        self.attack = 5
        self.sprite_sheet = pygame.image.load('Legacy-Fantasy-High-Forest-2.3/Character/Run/Run-Sheet.png')
        self.image = self.get_image(16, 16)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.vel_y = 0
        self.gravity = 0.001
        self.jump_force = - 0.6
        self.on_ground = True

    def move_right(self):  self.position[0] += self.speed
    def move_left(self):  self.position[0] -= self.speed
    
    def move_jump(self):
        if self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False

    def update(self):
        self.vel_y += self.gravity
        self.position[1] += self.vel_y

        if self.position[1] > 640 - 48:
            self.position[1] = 640 - 48
            self.on_ground = True

        self.rect.topleft = self.position    

    def get_image(self, x, y):
        image = pygame.Surface([48, 48])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 48, 48))   
        print(image.get_size())
        return image

        
