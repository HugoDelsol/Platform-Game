import pygame
import pytmx
import pyscroll

class Tmx_map(pygame.sprite.Sprite):

    def __init__(self, screen, player):
        super().__init__()
        self.screen = screen
        self.player = player
        self.tmx_data = None
        self.map_layer = None
        self.group = None
        self.gravity = None
        self.walls = []    
        self.load_map("map3")    

    def load_map(self, map_name: str): 
        tmx_data = pytmx.load_pygame(f'Legacy-Fantasy-High-Forest-2.3/map/{map_name}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)
        for obj in tmx_data.objects:            
            if obj.type == 'col':
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
                print(self.walls)
    

    def update(self):
        
        self.player.rect.x = self.player.position[0]
        self.player.feet.midbottom = self.player.rect.midbottom

        for wall in self.walls:
            if self.player.feet.colliderect(wall):
                
                if self.player.rect.centerx < wall.centerx:
                    self.player.move_back()                
                else:
                    self.player.move_back()               
                
                self.player.rect.x = self.player.position[0]
                self.player.feet.midbottom = self.player.rect.midbottom
        
        self.player.update() 
        self.player.rect.y = self.player.position[1]
        self.player.feet.midbottom = self.player.rect.midbottom

        for wall in self.walls:
            if self.player.feet.colliderect(wall):
                if self.player.feet.bottom >= wall.top:
                    self.player.move_back()
                    self.player.vel_y = 0
                    self.player.on_ground = True 
                
                self.player.rect.y = self.player.position[1]
                self.player.feet.midbottom = self.player.rect.midbottom
       
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())
        
    