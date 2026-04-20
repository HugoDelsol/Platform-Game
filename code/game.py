import pygame
import pytmx
import pyscroll

class Game:         

    def __init__(self, screen, player):
        self.player = player        
        self.screen = screen
        self.load_map() 

    def load_map(self):
        self.map_name = "map3"
        tmx_data = pytmx.load_pygame(f'Legacy-Fantasy-High-Forest-2.3/map/{self.map_name}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def update(self):
        self.group.center(self.player.rect.center)
        surface = self.screen.get_display()
        self.group.draw(surface) 
   
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if (pressed[pygame.K_RIGHT]):
            self.player.move_right()
        if (pressed[pygame.K_LEFT]):
            self.player.move_left()
        if (pressed[pygame.K_UP]):
            self.player.move_jump()
        if (pressed[pygame.K_DOWN]):
            self.player.move_down()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running=False

    def run(self, ):
        self.running = True
        while self.running:
            self.player.update()
            self.handle_input()
            self.update() 
            pygame.display.flip()          