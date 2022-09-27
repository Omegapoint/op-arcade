import pygame
pygame.init()

import os
from arcade_lib.constants import COLOR_BLACK, COLOR_GRAY, COLOR_BLUE, COLOR_GREEN, COLOR_RED, COLOR_WHITE, COLOR_CYAN, COLOR_MAGENTA, COLOR_YELLOW
from arcade_lib.arcade_inputs import ArcadeInput
from games.demo.player import Player

if os.environ.get("OP_ARCADE"):
  inputs = ArcadeInput("OP_ARCADE")
else:
  inputs = ArcadeInput("KEYBOARD")

main_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

players = []
players.append(Player(COLOR_RED, inputs.player_inputs[0], 100, 100))
players.append(Player(COLOR_BLUE, inputs.player_inputs[1], 200, 100))
players.append(Player(COLOR_GREEN, inputs.player_inputs[2], 300, 100))
players.append(Player(COLOR_CYAN, inputs.player_inputs[3], 100, 200))
players.append(Player(COLOR_MAGENTA, inputs.player_inputs[4], 100, 300))
players.append(Player(COLOR_YELLOW, inputs.player_inputs[5], 200, 200))
players.append(Player(COLOR_BLACK, inputs.player_inputs[6], 200, 300))
players.append(Player(COLOR_GRAY, inputs.player_inputs[7], 300, 200))

while True:
  
  inputs.update() # Call early. Must be called to update events (also joystick input hangs if this is not called)
  time_since_last_tick = clock.tick(60) # Max 60 fps
  delta_time_seconds = time_since_last_tick / 1000.0

  main_surface.fill(COLOR_WHITE)

  for player in players:
    player.update(delta_time_seconds)
    player.draw(main_surface)

  pygame.display.flip()
