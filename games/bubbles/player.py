from __future__ import annotations
from typing import TYPE_CHECKING

from games.bubbles.update_results import UpdateResult
if TYPE_CHECKING:
  from games.bubbles.bubble import Bubble
  from games.bubbles.game import Game
from games.bubbles.hook import Hook
from games.bubbles.vector2 import Vector2
from games.bubbles.world import WorldProps, to_surface_coordinates
import math
import arcade_lib.arcade_inputs
import pygame


class Player():

  _COLLISSION_RADIUS = 10
  _CHARACTER_RADIUS = 15
  _ANGULAR_SPEED = (math.pi * 2) / 8

  def __init__(self, start_angle : float, color, inputs : arcade_lib.arcade_inputs.ArcadePlayerInput, world_props : WorldProps):
    self.inputs : arcade_lib.arcade_inputs.ArcadePlayerInput = inputs
    self.color = color
    self.angle : float = start_angle
    self.world_props : WorldProps = world_props
    self.hook : Hook = None

  def calc_pos(self) -> Vector2:
    character_height = Player._CHARACTER_RADIUS
    return Vector2(math.cos(self.angle), math.sin(self.angle)).multiply(self.world_props.outer_radius - character_height) 

  def update(self, deltaTime : float, game : Game) -> UpdateResult:
    if self.inputs.get_left_button_state():
      self.angle = (self.angle + Player._ANGULAR_SPEED * deltaTime) % (math.pi * 2)
    if self.inputs.get_right_button_state():
      self.angle = (self.angle - Player._ANGULAR_SPEED * deltaTime) % (math.pi * 2)
    if self.inputs.get_action_button_down():
      if self.hook == None:
        self.shoot(game)
    for bubble in game.world.bubbles:
      if self.collided_with_bubble(bubble):
        return UpdateResult.KILLME
    return UpdateResult.NONE


  def draw(self, surface : pygame.Surface) -> None:
    pos = self.calc_pos()
    pygame.draw.circle(surface, self.color, to_surface_coordinates(pos), Player._CHARACTER_RADIUS)

  def shoot(self, game : Game) -> None:
    self.hook = Hook(self.angle, self.world_props.outer_radius, self)
    game.register_hook(self.hook)

  def unregister_hook(self):
    self.hook = None

  def collided_with_bubble(self, bubble : Bubble) -> bool:
    return self.calc_pos().distance(bubble.calc_pos()) < max(Player._COLLISSION_RADIUS, bubble.size)