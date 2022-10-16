from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from games.bubbles.game import Game


import pygame
import os
import math
from games.bubbles.game_object import GameObject
from arcade_lib.spritesheet import AnimationState, Spritesheet, SpritesheetAnimation
from arcade_lib.vector2 import Vector2
from games.bubbles.util import get_centered_sprite_pos, to_surface_coordinates


splash_sheet_path = os.path.join(os.path.dirname(__file__), "assets", "bloodsplatter.png")
splash_spritesheet = Spritesheet(splash_sheet_path, 200, 200)
splatter_sheet_path = os.path.join(os.path.dirname(__file__), "assets", "dropsplash.png")
splatter_spritesheet = Spritesheet(splatter_sheet_path,  118, 148)

class BloodSplatter(GameObject):
  def __init__(self, position : Vector2, angle : float):
    self.surface_position : Vector2 = to_surface_coordinates(position)
    self.angle : float = angle
    self.splash_animation = SpritesheetAnimation(splash_spritesheet, [(0,3),(1,3),(2,3),(3,3),(0,2),(1,2),(2,2),(3,2),(0,1),(1,1),(2,1),(3,1),(0,0),(1,0),(2,0),(3,0)], fps = 35, is_looping = False, is_flipped=False)
    self.splash_animation.restart()    
    self.splatter_animation = SpritesheetAnimation(splatter_spritesheet, [(0, 0), (0, 1), (0, 2)], fps = 10, is_looping = False, is_flipped=False)
    self.splatter_animation.restart()

  def update(self, delta_time : float, game : Game):
    self.splash_animation.update(delta_time)
    self.splatter_animation.update(delta_time)
    #if self.splash_animation.state == AnimationState.FINISHED:
    #  game.destroy_gameobject(self)

  def draw(self, surface : pygame.Surface):
    current_image = self.splatter_animation.get_current_image()
    if (self.splash_animation.state != AnimationState.FINISHED):
      current_image.blit(self.splash_animation.get_current_image(), (-25,0))
    current_image = pygame.transform.rotate(current_image, -math.degrees(self.angle) + 90)
    sprite_pos = get_centered_sprite_pos(current_image, self.surface_position)
    surface.blit(current_image, tuple(sprite_pos))
