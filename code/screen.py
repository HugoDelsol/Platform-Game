import pygame

class Screen:

    def __init__(self):
        self.title = pygame.display.set_caption("Pygame")
        self.screen =  pygame.display.set_mode((640,640))

    def get_display(self):
        return self.screen
    
    def get_size(self):
        print(self.screen.get_size())
        return self.screen.get_size()
