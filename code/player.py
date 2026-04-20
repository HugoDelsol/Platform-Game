import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 0.2
        self.attack = 5
        self.sprite_sheet = pygame.image.load('Legacy-Fantasy-High-Forest-2.3/Character/Run/Run-Sheet.png')
        self.image = self.get_image(16, 16)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]

    def move_right(self):  self.position[0] += self.velocity
    def move_left(self):  self.position[0] -= self.velocity
    def move_jump(self):  self.position[1] -= self.velocity 
    def move_down(self):  self.position[1] += self.velocity 

    def update(self):
        self.rect.topleft = self.position

    def get_image(self, x, y):
        image = pygame.Surface([48, 48])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 48, 48))   
        print(image.get_size())
        return image

        
