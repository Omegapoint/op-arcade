import pygame

from arcade_lib.vector2 import Vector2
from games.bubbles.util import to_surface_coordinates, circle_line_segment_intersection

# TODO: Walls currently only works if they completely block a full angle. There can be no gaps with the current implementation.
class Wall:
  def __init__(self, angle : float, start_radius : float, end_radius : float):
    self.angle = angle
    self.start_radius = start_radius
    self.end_radius = end_radius
    self.__start_pos = Vector2.from_radial(self.start_radius, self.angle)
    self.__end_pos = Vector2.from_radial(self.end_radius, self.angle)

  def draw(self, surface : pygame.Surface):
    pygame.draw.line(surface, [50, 50, 50], tuple(to_surface_coordinates(self.__start_pos)), tuple(to_surface_coordinates(self.__end_pos)), 4)

  def hit_with_circle(self, center : Vector2, radius : float):
    return circle_line_segment_intersection(circle_center = center, circle_radius = radius, pt1 = self.__start_pos, pt2=self.__end_pos)
