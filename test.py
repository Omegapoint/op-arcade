from pickle import TRUE
import pygame
from arcade_lib.arcade_inputs import ArcadeInput
import os
import math
from arcade_lib.vector2 import Vector2

def main():
  inputs : list[ArcadeInput] = None
  if os.environ.get("OP_ARCADE"):
    inputs = ArcadeInput("OP_ARCADE")
  else:
    inputs = ArcadeInput("KEYBOARD")

  main_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
  clock = pygame.time.Clock()

  from arcade_lib.spritesheet import Spritesheet, SpritesheetAnimation
  from games.bubbles.blood_splatter import BloodSplatter
  sheet_path = os.path.join(os.path.dirname(__file__), "games", "bubbles", "assets", "bloodsplatter.png")
  spritesheet = Spritesheet(sheet_path, 200, 200)
  animation = SpritesheetAnimation(spritesheet, [(0,3),(1,3),(2,3),(3,3),(0,2),(1,2),(2,2),(3,2),(0,1),(1,1),(2,1),(3,1),(0,0),(1,0),(2,0),(3,0)], fps = 35, is_looping = True, is_flipped=False)
  animation.restart()
  while True:
    delta_time_millis = clock.tick()
    delta_time = delta_time_millis / 1000
    main_surface.fill([255,255,255])

    animation.update(delta_time)
    current_image = animation.get_current_image()
    current_image = pygame.transform.rotate(current_image, 0)
    
    main_surface.blit(current_image, (500, 500))

    pygame.display.flip()


main()