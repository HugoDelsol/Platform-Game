import pygame
pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.health = 100
        self.max_health = 100
        self.speed = 0.1
        self.attack = 5
        self.sprite_sheet = pygame.image.load('Legacy-Fantasy-High-Forest-2.3/Character/Run/Run-Sheet.png')
        self.image = self.get_image(16, 16)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [screen.get_size()[0] - screen.get_size()[0] + 50, 0]
        self.vel_y = 0
        self.gravity = 0.0001
        self.jump_force = -0.2
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 2)        
        self.on_ground = True

    def move_right(self):  self.position[0] += self.speed
    def move_left(self):  self.position[0] -= self.speed

    def save_location(self):
        self.rect.topleft = self.position

    def move_back(self):
        self.position = self.old_pos
    
    def move_jump(self):
        if self.on_ground:
            self.vel_y = self.jump_force
            self.on_ground = False

    def update(self):
        self.old_pos = self.position.copy()
        self.vel_y += self.gravity
        self.position[1] += self.vel_y        

    def get_image(self, x, y):
        image = pygame.Surface([48, 48])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 48, 48))   
        print(image.get_size())
        return image

        
