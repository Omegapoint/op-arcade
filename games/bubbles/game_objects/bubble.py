from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from games.bubbles.world import World

from enum import Enum
from games.bubbles.game_objects.wall import Wall
from games.bubbles.util import to_surface_coordinates
from arcade_lib.vector2 import Vector2
import pygame

class BubbleSpecs:
  def __init__(self, size : int, color : tuple[int, int, int]):
    self.size : int = size
    self.color : tuple[int, int, int] = color

class BubbleType(Enum):
  BIG_NORMAL = BubbleSpecs(100, [125,0,0])
  MEDIUM_NORMAL = BubbleSpecs(50, [125,125,0])
  SMALL_NORMAL = BubbleSpecs(25, [125,0,125])
  TINY_NORMAL = BubbleSpecs(10, [255,0,0])
  FOUR_TINIES = BubbleSpecs(40, [125,0,255])
  EIGHT_TINIES = BubbleSpecs(80, [125,255,0])

class Bubble:

  RADIAL_ACCELERATION = 100

  def __init__(self, 
        angular_pos : float, 
        radial_pos: float, 
        tangential_velocity : float, 
        type : BubbleType):
    self.angular_pos : float = angular_pos
    self.radial_pos : float = radial_pos
    self.radial_velocity : float = 0
    self.tangential_velocity : float = tangential_velocity
    self.target_tangential_velocity = self.tangential_velocity
    self.size : float = type.value.size
    self.color : tuple[int, int, int] = type.value.color
    self.score = 5
    self.type = type

  def set_target_tangential_velocity(self, target_tangential_velocity):
    self.target_tangential_velocity = target_tangential_velocity

  def update_radial(self, delta_time: float, world_outer_bound : float):
    self.radial_velocity += Bubble.RADIAL_ACCELERATION * delta_time
    next_radial = self.radial_pos + self.radial_velocity * delta_time
    if next_radial + self.size > world_outer_bound:
      # Bounce
      self.radial_velocity = -self.radial_velocity
      rdiff = next_radial - self.radial_pos
      next_radial = (2 * world_outer_bound) - rdiff - self.radial_pos - (2 * self.size)
    self.radial_pos = next_radial

  def update_angular(self, delta_time : float, walls : tuple[Wall]):
    if abs(self.tangential_velocity - self.target_tangential_velocity) > 0.001:
      self.tangential_velocity += (self.target_tangential_velocity - self.tangential_velocity) * delta_time
    next_angle = self.angular_pos + self.tangential_velocity * delta_time
    next_pos = Vector2.from_radial(self.radial_pos, next_angle)
    for wall in walls:
      if wall.hit_with_circle(next_pos, self.size):
        # Bounce
        self.tangential_velocity *= -1
        self.target_tangential_velocity *= -1
    self.angular_pos += self.tangential_velocity * delta_time # TODO: This is a bit wrong.

  def update(self, delta_time: float, world : World):
    self.update_radial(delta_time, world.outer_radius)
    self.update_angular(delta_time, world.walls)
    
  def calc_pos(self) -> Vector2:
    return Vector2.from_radial(self.radial_pos, self.angular_pos)

  def draw(self, surface : pygame.Surface) -> None:
    pygame.draw.circle(surface, self.color, tuple(to_surface_coordinates(self.calc_pos())), self.size)
    pygame.draw.circle(surface, [0,0,0], tuple(to_surface_coordinates(self.calc_pos())), self.size, 2)

  def get_spawns(self):
    if self.type == BubbleType.BIG_NORMAL:
      return [
        Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity, type = BubbleType.MEDIUM_NORMAL),
        Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity, type = BubbleType.MEDIUM_NORMAL)
      ]
    elif self.type == BubbleType.MEDIUM_NORMAL:
      return [
        Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity, type = BubbleType.SMALL_NORMAL),
        Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity, type = BubbleType.SMALL_NORMAL)
      ]
    elif self.type == BubbleType.SMALL_NORMAL:
      return [
        Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity, type = BubbleType.TINY_NORMAL),
        Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity, type = BubbleType.TINY_NORMAL)
      ]
    elif self.type == BubbleType.TINY_NORMAL:
      return []
    elif self.type == BubbleType.FOUR_TINIES:
      b1 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity, type = BubbleType.TINY_NORMAL)
      b2 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL)
      b2.set_target_tangential_velocity(self.tangential_velocity)
      b3 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity, type = BubbleType.TINY_NORMAL)
      b4 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL)
      b4.set_target_tangential_velocity(-self.tangential_velocity)
      return [b1, b2, b3, b4]
    elif self.type == BubbleType.EIGHT_TINIES:
      b1 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity, type = BubbleType.TINY_NORMAL)
      b2 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL)
      b2.set_target_tangential_velocity(self.tangential_velocity)
      b3 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity / 3, type = BubbleType.TINY_NORMAL)
      b3.set_target_tangential_velocity(self.tangential_velocity)
      b4 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = self.tangential_velocity / 4, type = BubbleType.TINY_NORMAL)
      b4.set_target_tangential_velocity(self.tangential_velocity)
      b5 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity, type = BubbleType.TINY_NORMAL)
      b6 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL)
      b6.set_target_tangential_velocity(-self.tangential_velocity)
      b7 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity / 3, type = BubbleType.TINY_NORMAL)
      b7.set_target_tangential_velocity(-self.tangential_velocity)
      b8 = Bubble(angular_pos=self.angular_pos, radial_pos=self.radial_pos, tangential_velocity = -self.tangential_velocity / 4, type = BubbleType.TINY_NORMAL)
      b8.set_target_tangential_velocity(-self.tangential_velocity)
      return[b1, b2, b3, b4, b5, b6, b7, b8]