from pickle import TRUE
import pygame
from arcade_lib.arcade_inputs import ArcadeInput
import os
import math
from arcade_lib.vector2 import Vector2
from games.bubbles.util import get_centered_sprite_pos

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
  blood_animation = SpritesheetAnimation(spritesheet, [(0,3),(1,3),(2,3),(3,3),(0,2),(1,2),(2,2),(3,2),(0,1),(1,1),(2,1),(3,1),(0,0),(1,0),(2,0),(3,0)], fps = 35, is_looping = True, is_flipped=False)
  blood_animation.restart()

  hit_sheet_path = os.path.join(os.path.dirname(__file__), "games", "bubbles", "assets", "hit_with_ring_yellow.png")
  hit_spritesheet = Spritesheet(hit_sheet_path, 150, 150)
  hit_animation = SpritesheetAnimation(hit_spritesheet, [(0,0), (0, 1),(0,2), (0, 3), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3)], fps = 40, is_looping = True, is_flipped=False)
  hit_animation.restart()

  while True:
    delta_time_millis = clock.tick()
    delta_time = delta_time_millis / 1000
    main_surface.fill([200,200,200])

    blood_animation.update(delta_time)
    blood_image = blood_animation.get_current_image()
    blood_image = pygame.transform.rotate(blood_image, 0)
    main_surface.blit(blood_image, (500, 500))

    hit_animation.update(delta_time)
    hit_image = hit_animation.get_current_image()
    hit_image = pygame.transform.rotate(hit_image, 0)
    hit_center = Vector2(900, 900)
    sprite_pos = get_centered_sprite_pos(hit_image, hit_center)
    pygame.draw.circle(main_surface, [100,100,100], tuple(hit_center), 6, 6)
    main_surface.blit(hit_image, tuple(sprite_pos))

    pygame.display.flip()


main()