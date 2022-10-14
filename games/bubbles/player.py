from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING
from arcade_lib.spritesheet import Animator, Spritesheet, SpritesheetAnimation

from games.bubbles.update_results import UpdateResult
if TYPE_CHECKING:
  from games.bubbles.bubble import Bubble
  from games.bubbles.game import Game
from games.bubbles.hook import Hook
from arcade_lib.vector2 import Vector2
from games.bubbles.util import to_surface_coordinates
from games.bubbles.world import WorldProps
import math
import arcade_lib.arcade_inputs
import pygame
import os

sheet_path = os.path.join(os.path.dirname(__file__), "assets", "daxbotsheet.png")
player_spritesheet = Spritesheet(sheet_path, 64, 68)

class PlayerAnimationState(Enum):
  IDLE = 0
  WALKING_RIGHT = 1
  WALKING_LEFT = 2
  SHOOTING = 3

class Player():

  _HITBOX_CENTER_HEIGHT = 35
  _SPRITE_OFFSET = 27
  _HITBOX_RADIUS = 15
  _ANGULAR_SPEED = (math.pi * 2) / 8

  def __init__(self, start_angle : float, color, inputs : arcade_lib.arcade_inputs.ArcadePlayerInput, world_props : WorldProps):
    self.inputs : arcade_lib.arcade_inputs.ArcadePlayerInput = inputs
    self.color = color
    self.angle : float = start_angle
    self.world_props : WorldProps = world_props
    self.hook : Hook = None
    self.animator : Animator = self.create_animator()
    
  def create_animator(self) -> Animator:
    idle_animation = SpritesheetAnimation(player_spritesheet, [(0,0)], 1)
    walk_left_animation = SpritesheetAnimation(player_spritesheet, [(0,1),(0,2),(0,3),(1,1),(1,2),(1,3)], 10, is_flipped=True)
    walk_right_animation = SpritesheetAnimation(player_spritesheet, [(0,1),(0,2),(0,3),(1,1),(1,2),(1,3)], 10)
    return Animator({
      PlayerAnimationState.IDLE : idle_animation, 
      PlayerAnimationState.WALKING_LEFT : walk_left_animation,
      PlayerAnimationState.WALKING_RIGHT : walk_right_animation},
      initial_state=PlayerAnimationState.IDLE)

  def calc_hitbox_center_pos(self) -> Vector2:
    return Vector2(math.cos(self.angle), math.sin(self.angle)).multiply(self.world_props.outer_radius - Player._HITBOX_CENTER_HEIGHT) 

  def calc_sprite_pos(self) -> tuple[Vector2, Vector2]:
    return Vector2(math.cos(self.angle), math.sin(self.angle)).multiply(self.world_props.outer_radius - Player._SPRITE_OFFSET) 

  def update(self, deltaTime : float, game : Game) -> UpdateResult:
    idle = True
    if self.inputs.get_left_button_state():
      self.angle = (self.angle + Player._ANGULAR_SPEED * deltaTime) % (math.pi * 2)
      self.animator.set_state(PlayerAnimationState.WALKING_LEFT)
      idle = False
    if self.inputs.get_right_button_state():
      self.angle = (self.angle - Player._ANGULAR_SPEED * deltaTime) % (math.pi * 2)
      self.animator.set_state(PlayerAnimationState.WALKING_RIGHT)
      idle = False
    if self.inputs.get_action_button_down():
      if self.hook == None:
        self.shoot(game)
    for bubble in game.world.bubbles:
      if self.collided_with_bubble(bubble):
        return UpdateResult.KILLME
    if idle:
      self.animator.set_state(PlayerAnimationState.IDLE)
    return UpdateResult.NONE

  def draw(self, surface : pygame.Surface) -> None:
    # pygame.draw.circle(surface, self.color, to_surface_coordinates(self.calc_hitbox_center_pos()), Player._HITBOX_RADIUS) # <- the actual hitbox
    current_animation_image = self.animator.get_current_image()
    current_animation_image = pygame.transform.rotate(current_animation_image, -math.degrees(self.angle) + 90)
    surface_coordinates = list(to_surface_coordinates(self.calc_sprite_pos()))
    surface_coordinates[0] -= current_animation_image.get_width() / 2
    surface_coordinates[1] -= current_animation_image.get_height() / 2
    surface.blit(current_animation_image, surface_coordinates)

  def shoot(self, game : Game) -> None:
    self.hook = Hook(self.angle, self.world_props.outer_radius, self)
    game.register_hook(self.hook)

  def unregister_hook(self):
    self.hook = None

  def collided_with_bubble(self, bubble : Bubble) -> bool:
    return self.calc_hitbox_center_pos().distance(bubble.calc_pos()) < max(Player._HITBOX_RADIUS, bubble.size)