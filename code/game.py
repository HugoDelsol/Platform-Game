import pygame


class Game:         

    def __init__(self, screen, player, tmx_map):
        self.player = player        
        self.screen = screen
        self.tmx_map = tmx_map
   
    def handle_input(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running=False

            elif event.type == pygame.KEYDOWN:

                if (event.key == pygame.K_UP):
                    self.player.move_jump()
                    
                if event.key == pygame.K_ESCAPE:
                    self.running=False
                    
        pressed = pygame.key.get_pressed()

        if (pressed[pygame.K_RIGHT]):
            self.player.move_right()
        if (pressed[pygame.K_LEFT]):
            self.player.move_left()        
        if (pressed[pygame.K_DOWN]):
            self.player.move_down()
            

    def run(self, ):
        self.running = True
        while self.running:
            self.player.update()
            self.handle_input()
            self.tmx_map.update() 
            pygame.display.flip()   
