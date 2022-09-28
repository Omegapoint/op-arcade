import pygame

from games.pong8.ball import Ball
pygame.init()

import os
import math
from arcade_lib.constants import SCREEN_HEIGHT, SCREEN_WIDTH, COLOR_BLACK, COLOR_GRAY, COLOR_BLUE, COLOR_GREEN, COLOR_RED, COLOR_WHITE, COLOR_CYAN, COLOR_MAGENTA, COLOR_YELLOW
from arcade_lib.arcade_inputs import ArcadeInput
from games.pong8.player import Player

if os.environ.get("OP_ARCADE"):
  inputs = ArcadeInput("OP_ARCADE")
else:
  inputs = ArcadeInput("KEYBOARD")

main_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

players = []
players.append(Player(inputs.player_inputs[0], 100, 100, 0 * math.pi / 4))
players.append(Player(inputs.player_inputs[1], 200, 100, 1 * math.pi / 4))
players.append(Player(inputs.player_inputs[2], 300, 100, 2 * math.pi / 4))
players.append(Player(inputs.player_inputs[3], 100, 200, 3 * math.pi / 4))
players.append(Player(inputs.player_inputs[4], 100, 300, 4 * math.pi / 4))
players.append(Player(inputs.player_inputs[5], 200, 200, 5 * math.pi / 4))
players.append(Player(inputs.player_inputs[6], 200, 300, 6 * math.pi / 4))
players.append(Player(inputs.player_inputs[7], 300, 200, 7 * math.pi / 4))

balls = []
def spawnBall():
  ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100)
  return ball

BALL_SPAWN_TIME = 1
time_since_last_ball = 0

while True:
  inputs.update() # Call early. Must be called to update events (also joystick input hangs if this is not called)
  time_since_last_tick = clock.tick(60) # Max 60 fps
  delta_time_seconds = time_since_last_tick / 1000.0

  main_surface.fill(COLOR_BLACK)

  time_since_last_ball += time_since_last_tick
  if time_since_last_ball >= BALL_SPAWN_TIME:
    balls.append(spawnBall())
    time_since_last_ball = 0

  for player in players:
    player.update(delta_time_seconds)
    player.draw(main_surface)

  for ball in balls:
    ball.update(delta_time_seconds, players)
    ball.draw(main_surface)

  pygame.display.flip()
