import pygame
from games.bubbles.game import Game
from arcade_lib.arcade_inputs import ArcadeInput
import os

def main():
  inputs : list[ArcadeInput] = None
  if os.environ.get("OP_ARCADE"):
    inputs = ArcadeInput("OP_ARCADE")
  else:
    inputs = ArcadeInput("KEYBOARD")

  pygame.init()
  main_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  clock = pygame.time.Clock()

  game = Game(inputs, start_from_level=3)

  while True:
    delta_time_millis = clock.tick()
    delta_time = delta_time_millis / 1000
    game.update(delta_time)
    game.draw(main_surface)
    pygame.display.flip()


