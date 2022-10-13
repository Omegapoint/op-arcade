from games.bubbles.bubble import Bubble
from games.bubbles.util import to_surface_coordinates
from games.bubbles.vector2 import Vector2
import pygame
import math



class WorldProps:
  def __init__(self, outer_radius : int, inner_radius : int):
    self.outer_radius : int = outer_radius
    self.inner_radius : int = inner_radius


class World:
  def __init__(self, level : int):
    self.props : WorldProps = self.__init_props(level)
    self.bubbles : list[Bubble] = self.__init_bubbles(level)

  def __init_props(self, level : int):
    return WorldProps(500, 100)

  def __init_bubbles(self, level : int):
    return [Bubble(90, 200, 100, math.pi * 2 / 16)]

  def update(self, delta_time : float):
    for bubble in self.bubbles:
      bubble.update(delta_time, self)

  def bubble_hit(self, bubble : Bubble):
    new_size = bubble.size / 2
    self.bubbles.remove(bubble)
    if (new_size > Bubble.SMALLEST_RADIUS):
      self.bubbles.append(Bubble(start_angle=bubble.angle, start_radius=bubble.radius, size=new_size, tangential_velocity = bubble.tangential_velocity))
      self.bubbles.append(Bubble(start_angle=bubble.angle, start_radius=bubble.radius, size=new_size, tangential_velocity = -bubble.tangential_velocity))

  def draw(self, surface : pygame.Surface) -> None:
    surface.fill([0,0,0])
    pygame.draw.circle(surface, [255, 255, 255], to_surface_coordinates(Vector2()), self.props.inner_radius, 2)
    pygame.draw.circle(surface, [255, 255, 255], to_surface_coordinates(Vector2()), self.props.outer_radius, 2)
    for bubble in self.bubbles:
      bubble.draw(surface)
