import pygame

from games.pong8.ball import Ball
from games.pong8.update_results import UpdateResult
pygame.init()

import os
import math
from arcade_lib.constants import SCREEN_HEIGHT, SCREEN_WIDTH, COLOR_BLACK, COLOR_GRAY, COLOR_BLUE, COLOR_GREEN, COLOR_RED, COLOR_WHITE, COLOR_CYAN, COLOR_MAGENTA, COLOR_YELLOW
from arcade_lib.arcade_inputs import ArcadeInput
from games.pong8.player import Player

def spawnBall():
  ball = Ball(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 100)
  return ball

BALL_SPAWN_TIME = 1


def is_game_over(players):
  num_still_alive = len([player for player in players if player.is_alive()])
  return num_still_alive < 2

def draw_intro(surface):
  surface.fill(COLOR_BLACK)
  font = pygame.font.Font('freesansbold.ttf', 20)
  lives_text_obj = font.render("Tryck på stora knappen för att starta", False, [255, 255, 255])
  rotatedSurf = pygame.transform.rotate(lives_text_obj, 0)
  rotatedRect = rotatedSurf.get_rect()
  rotatedRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  surface.blit(rotatedSurf, rotatedRect)
  pygame.display.flip()

def draw_game_over(surface, players, balls):
  surface.fill(COLOR_BLACK)
  for player in players:
    player.draw(surface)
  for ball in balls:
    ball.draw(surface)
  font = pygame.font.Font('freesansbold.ttf', 20)
  lives_text_obj = font.render("Tryck på stora knappen för att starta om!", False, [255, 255, 255])
  rotatedSurf = pygame.transform.rotate(lives_text_obj, 0)
  rotatedRect = rotatedSurf.get_rect()
  rotatedRect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  surface.blit(rotatedSurf, rotatedRect)
  pygame.display.flip()

def main():
  if os.environ.get("OP_ARCADE"):
    inputs = ArcadeInput("OP_ARCADE")
  else:
    inputs = ArcadeInput("KEYBOARD")

  main_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  clock = pygame.time.Clock()

  draw_intro(main_surface)

  while True:

    
    # Wait for start
    inputs.update()
    if not inputs.get_start_button_state():
      continue

    players : list[Player]= []
    cx = SCREEN_WIDTH / 2
    cy = SCREEN_HEIGHT / 2
    for i in range(8):
      players.append(Player(inputs.player_inputs[i], (-i + 2) * math.pi / 4))

    balls = []
    time_since_last_ball = 0
    
    while not is_game_over(players):
      inputs.update() # Call early. Must be called to update events (also joystick input hangs if this is not called)
      time_since_last_tick = clock.tick(60) # Max 60 fps
      delta_time_seconds = time_since_last_tick / 1000.0

      main_surface.fill(COLOR_BLACK)

      time_since_last_ball += delta_time_seconds
      if time_since_last_ball >= BALL_SPAWN_TIME:
        if len(balls) > 100: # reasonable number of balls right
          balls.pop()
        balls.append(spawnBall())
        time_since_last_ball = 0

      for player in players:
        player.update(delta_time_seconds)
        player.draw(main_surface)

      for ball in balls:
        update_result = ball.update(delta_time_seconds, players)
        if update_result == UpdateResult.KILLME:
          balls.remove(ball)
          if is_game_over(players):
            draw_game_over(main_surface, players, balls)
            break
        else:
          ball.draw(main_surface)

      pygame.display.flip()

main()
