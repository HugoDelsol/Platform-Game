import pytmx
import pyscroll

class Tmx_map():

    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.tmx_data = None
        self.map_layer = None
        self.group = None
        self.gravity = None
        self.load_map("map3")       

    def load_map(self, map_name: str): 
        tmx_data = pytmx.load_pygame(f'Legacy-Fantasy-High-Forest-2.3/map/{map_name}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def update(self):
        self.group.center(self.player.rect.center)
        surface = self.screen.get_display()
        self.group.draw(surface) 
        