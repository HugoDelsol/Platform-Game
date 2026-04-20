import pygame
pygame.init()

from game import Game
from screen import Screen
from player import Player

screen = Screen()

screen_height = screen.get_size()[1]
screen_width = screen.get_size()[0]

print(screen_height)

player = Player(screen_width - screen_width, screen_height - 48)
game = Game(screen, player)

if __name__ == "__main__":
    game.run()

pygame.quit()