from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from games.bubbles.game import Game

import random
import pygame
import os
import math
from games.bubbles.game_object import GameObject
from arcade_lib.spritesheet import AnimationState, Spritesheet, SpritesheetAnimation
from arcade_lib.vector2 import Vector2
from games.bubbles.util import get_centered_sprite_pos, to_surface_coordinates


hit_sheet_path = os.path.join(os.path.dirname(__file__), "assets", "hit_with_ring_yellow.png")
hit_spritesheet = Spritesheet(hit_sheet_path, 150, 150)

class HitMarker(GameObject):
  def __init__(self, position : Vector2):
    self.position : Vector2 = position
    self.hit_animation = SpritesheetAnimation(hit_spritesheet, [(0,0), (0, 1),(0,2), (0, 3), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3)], fps = 40, is_looping = False, is_flipped=False)
    self.hit_animation.restart()   
    self.angle = random.random() * 360

  def update(self, delta_time : float, game : Game):
    self.hit_animation.update(delta_time)
    if self.hit_animation.state == AnimationState.FINISHED:
      game.destroy_gameobject(self)

  def draw(self, surface : pygame.Surface):
    surface_pos = to_surface_coordinates(self.position)
    current_image = self.hit_animation.get_current_image()
    current_image = pygame.transform.rotate(current_image, self.angle)
    sprite_pos = get_centered_sprite_pos(current_image, surface_pos)
    surface.blit(current_image, tuple(sprite_pos))
