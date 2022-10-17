from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.world import World

from games.bubbles.util import to_surface_coordinates
from arcade_lib.vector2 import Vector2
import pygame

class BubbleProps:
  def __init__(self, size : int, color : tuple[int, int, int]):
    self.size : int = size
    self.color : tuple[int, int, int] = color

class BubbleType(Enum):
  BIG_NORMAL = BubbleProps(100, [125,0,0])
  MEDIUM_NORMAL = BubbleProps(50, [125,125,0])
  SMALL_NORMAL = BubbleProps(25, [125,0,125])
  TINY_NORMAL = BubbleProps(10, [255,0,0])
  FOUR_TINIES = BubbleProps(40, [125,0,255])
  EIGHT_TINIES = BubbleProps(80, [125,255,0])

class Bubble:

  SMALLEST_RADIUS = 25 - 0.001
  RADIAL_ACCELERATION = 100

  def __init__(self, 
        start_angle : float, 
        start_radius: float, 
        tangential_velocity : float, 
        type : BubbleType):
    self.angle : float = start_angle
    self.radius : float = start_radius
    self.radial_velocity : float = 0
    self.tangential_velocity : float = tangential_velocity
    self.size : float = type.value.size
    self.color : tuple[int, int, int] = type.value.color
    self.score = 5
    self.type = type

  def apply_gravity(self, delta_time: float):
    self.radial_velocity += Bubble.RADIAL_ACCELERATION * delta_time
    self.radius += self.radial_velocity * delta_time
    self.angle += self.tangential_velocity * delta_time

  def update(self, deltaTime: float, world : World):
    self.apply_gravity(deltaTime)
    if self.radius + self.size >= world.props.outer_radius:
      self.radius = world.props.outer_radius - self.size # TODO: might want to make this more exact (too tired to calculate this correctly even though it is easy)
      self.radial_velocity = - self.radial_velocity

  def calc_pos(self) -> Vector2:
    return Vector2.from_radial(self.radius, self.angle)

  def draw(self, surface : pygame.Surface) -> None:
    pygame.draw.circle(surface, self.color, tuple(to_surface_coordinates(self.calc_pos())), self.size)

  def get_spawns(self):
    if self.type == BubbleType.BIG_NORMAL:
      return [
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity, type = BubbleType.MEDIUM_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity, type = BubbleType.MEDIUM_NORMAL)
      ]
    elif self.type == BubbleType.MEDIUM_NORMAL:
      return [
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity, type = BubbleType.SMALL_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity, type = BubbleType.SMALL_NORMAL)
      ]
    elif self.type == BubbleType.SMALL_NORMAL:
      return [
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity, type = BubbleType.TINY_NORMAL)
      ]
    elif self.type == BubbleType.TINY_NORMAL:
      return []
    elif self.type == BubbleType.FOUR_TINIES:
      return [
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL)
      ]
    elif self.type == BubbleType.EIGHT_TINIES:
      return [
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity / 3, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = self.tangential_velocity / 4, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity / 2, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity / 3, type = BubbleType.TINY_NORMAL),
        Bubble(start_angle=self.angle, start_radius=self.radius, tangential_velocity = -self.tangential_velocity / 4, type = BubbleType.TINY_NORMAL)
      ]