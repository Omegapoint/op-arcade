from games.bubbles.bubble import Bubble, BubbleType
from games.bubbles.util import to_surface_coordinates
from arcade_lib.vector2 import Vector2
import pygame
import math

from games.bubbles.wall import Wall
from games.bubbles.world_specs import WORLD_SPECS
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)


class World:
  def __init__(self, level : int):
    specs = WORLD_SPECS[level]
    self.outer_radius = specs.outer_radius
    self.inner_radius = specs.inner_radius
    self.seconds_until_game_over = specs.seconds_until_game_over
    self.color = specs.color
    self.bubbles = specs.bubbles
    self.walls = specs.walls

  '''
  def __init_bubbles(self, level : int):
    if level == 1:
      return [Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL)]
    if level == 2:
      return [
        Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 12, type = BubbleType.MEDIUM_NORMAL),
        Bubble(start_angle = math.pi, start_radius = 200, tangential_velocity = math.pi * 2 / 12, type = BubbleType.MEDIUM_NORMAL),
      ]
    if level == 3:
      return [
        Bubble(start_angle = math.pi * 2 * 1 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi * 2 * 3 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
      ]
    if level == 4:
      return [
        Bubble(start_angle = math.pi * 2 * 0 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
        Bubble(start_angle = math.pi * 2 * 1 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
        Bubble(start_angle = math.pi * 2 * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
      ]
    if level == 5:
      return [
        Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.MEDIUM_NORMAL),
        Bubble(start_angle = 0, start_radius = 150, tangential_velocity = math.pi * 2 / 16, type = BubbleType.MEDIUM_NORMAL),
        Bubble(start_angle = math.pi * 2 / 3, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.MEDIUM_NORMAL),
        Bubble(start_angle = math.pi * 2  / 3, start_radius = 150, tangential_velocity = math.pi * 2 / 16, type = BubbleType.MEDIUM_NORMAL),
        Bubble(start_angle = math.pi * 2 * 2 / 3, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.MEDIUM_NORMAL),
        Bubble(start_angle = math.pi * 2 * 2 / 3, start_radius = 150, tangential_velocity = math.pi * 2 / 16, type = BubbleType.MEDIUM_NORMAL),
      ]
    if level == 6:
      return [
        Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
        Bubble(start_angle = math.pi * 2 * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
        Bubble(start_angle = math.pi * 2 * 3 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
      ]
    if level == 7:
      return [
        Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.EIGHT_TINIES),
        Bubble(start_angle = math.pi * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.EIGHT_TINIES),
        Bubble(start_angle = math.pi * 2 * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.EIGHT_TINIES),
        Bubble(start_angle = math.pi * 2 * 3 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.EIGHT_TINIES),
      ]
  '''

  def update(self, delta_time : float):
    for bubble in self.bubbles:
      bubble.update(delta_time, self)

  def bubble_hit(self, bubble : Bubble):
    self.bubbles.remove(bubble)
    for new_bubble in bubble.get_spawns():
      self.bubbles.append(new_bubble)

  def draw(self, surface : pygame.Surface) -> None:
    surface.fill(self.color)
    pygame.draw.circle(surface, [100, 255, 100], tuple(to_surface_coordinates(Vector2())), self.inner_radius, 4)
    pygame.draw.circle(surface, [255, 100, 255], tuple(to_surface_coordinates(Vector2())), self.outer_radius, 4)
    for wall in self.walls:
      wall.draw(surface)
    for bubble in self.bubbles:
      bubble.draw(surface)