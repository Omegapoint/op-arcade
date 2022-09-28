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
cx = SCREEN_WIDTH / 2
cy = SCREEN_HEIGHT / 2
for i in range(8):
  players.append(Player(inputs.player_inputs[i], i * math.pi / 4))


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

  time_since_last_ball += delta_time_seconds
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
