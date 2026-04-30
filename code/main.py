import pygame
pygame.init()

from game import Game
from screen import Screen
from player import Player
from map import Tmx_map

screen = Screen()

screen_height = screen.get_size()[1]
screen_width = screen.get_size()[0]

print(screen_height)

player = Player(screen)
tmx_map = Tmx_map(screen, player)
game = Game(screen, player, tmx_map)

if __name__ == "__main__":
    game.run()

pygame.quit()