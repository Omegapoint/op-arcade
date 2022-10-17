from games.bubbles.bubble import Bubble, BubbleType
from games.bubbles.util import to_surface_coordinates
from arcade_lib.vector2 import Vector2
import pygame
import math

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)


class WorldProps:
  def __init__(self, outer_radius : int, inner_radius : int, seconds_until_game_over : float = 60):
    self.outer_radius : int = outer_radius
    self.inner_radius : int = inner_radius
    self.seconds_until_game_over : int = seconds_until_game_over


class World:
  def __init__(self, level : int):
    self.props : WorldProps = self.__init_props(level)
    self.bubbles : list[Bubble] = self.__init_bubbles(level)

  def __init_props(self, level : int):
    return WorldProps(500, 100, seconds_until_game_over = 60)

  def __init_bubbles(self, level : int):
    if level == 1:
      return [Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL)]
    if level == 2:
      return [
        Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
      ]
    if level == 3:
      return [
        Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi * 2 / 3, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi * 2 * 2 / 3, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
      ]
    if level == 4:
      return [
        Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
        Bubble(start_angle = math.pi * 2 * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi * 2 * 3 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
      ]

  def update(self, delta_time : float):
    for bubble in self.bubbles:
      bubble.update(delta_time, self)

  def bubble_hit(self, bubble : Bubble):
    self.bubbles.remove(bubble)
    for new_bubble in bubble.get_spawns():
      self.bubbles.append(new_bubble)

  def draw(self, surface : pygame.Surface) -> None:
    surface.fill([200,200,200])
    pygame.draw.circle(surface, [100, 255, 100], tuple(to_surface_coordinates(Vector2())), self.props.inner_radius, 2)
    pygame.draw.circle(surface, [255, 100, 255], tuple(to_surface_coordinates(Vector2())), self.props.outer_radius, 2)
    for bubble in self.bubbles:
      bubble.draw(surface)