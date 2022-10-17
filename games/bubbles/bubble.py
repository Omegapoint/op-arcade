from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.world import World

from games.bubbles.util import to_surface_coordinates
from arcade_lib.vector2 import Vector2
import pygame
import math


class Bubble:

  SMALLEST_RADIUS = 25 - 0.001
  RADIAL_ACCELERATION = 100

  def __init__(self, start_angle : float, start_radius: float, size: float, tangential_velocity : float):
    self.angle : float = start_angle
    self.radius : float = start_radius
    self.radial_velocity : float = 0
    self.tangential_velocity : float = tangential_velocity
    self.size : float = size
    self.score = 5

  def apply_gravity(self, delta_time: float):
    self.radial_velocity += Bubble.RADIAL_ACCELERATION * delta_time
    self.radius += self.radial_velocity * delta_time
    self.angle += self.tangential_velocity * delta_time

  def update(self, deltaTime: float, world : World):
    self.apply_gravity(deltaTime)
    if self.radius + self.size >= world.props.outer_radius:
      self.radius = world.props.outer_radius - self.size # TODO: might want to make this more exact (too tired to calculate this correctly even though it is easy)
      self.radial_velocity = - self.radial_velocity

    # collission detection etc etc etc

  def calc_pos(self) -> Vector2:
    return Vector2.from_radial(self.radius, self.angle)

  def draw(self, surface : pygame.Surface) -> None:
    pygame.draw.circle(surface, [0, 255, 255], tuple(to_surface_coordinates(self.calc_pos())), self.size)
