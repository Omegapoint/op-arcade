from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.game import Game
from games.bubbles.hook import Hook
from games.bubbles.vector2 import Vector2
from games.bubbles.world import WorldProps, to_surface_coordinates
import math
import arcade_lib.arcade_inputs
import pygame


class Player():

  _COLLISSION_RADIUS = 10
  _CHARACTER_RADIUS = 10
  _ANGULAR_SPEED = (math.pi * 2) / 8

  def __init__(self, start_angle : float, color, inputs : arcade_lib.arcade_inputs.ArcadePlayerInput, world_props : WorldProps):
    self.inputs : arcade_lib.arcade_inputs.ArcadePlayerInput = inputs
    self.color = color
    self.angle : float = start_angle
    self.world_props : WorldProps = world_props
    self.hook : Hook = None
    self.alive : bool = True

  def __calc_position(self) -> Vector2:
    return Vector2(math.cos(self.angle), math.sin(self.angle)).multiply(self.world_props.outer_radius) 

  def update(self, deltaTime : float, game : Game) -> None:
    if self.inputs.get_left_button_state():
      self.angle = (self.angle + Player._ANGULAR_SPEED * deltaTime) % (math.pi * 2)
    if self.inputs.get_right_button_state():
      self.angle = (self.angle - Player._ANGULAR_SPEED * deltaTime) % (math.pi * 2)
    if self.inputs.get_action_button_down():
      if self.hook == None:
        self.shoot(game)

  def draw(self, surface : pygame.Surface) -> None:
    pos = self.__calc_position()
    pygame.draw.circle(surface, self.color, to_surface_coordinates(pos), Player._CHARACTER_RADIUS)

  def shoot(self, game : Game) -> None:
    self.hook = Hook(self.angle, self.world_props.outer_radius, self)
    game.register_hook(self.hook)

  def unregister_hook(self):
    self.hook = None

  def collissionTest(self, otherPos : Vector2) -> bool:
    return self.__calc_position().distance(otherPos) < Player._COLLISSION_RADIUS

  def die(self) -> None:
    self.alive = False