from games.bubbles.game_objects.bubble import Bubble, BubbleType
from games.bubbles.util import to_surface_coordinates
from arcade_lib.vector2 import Vector2
import pygame
import math

from games.bubbles.game_objects.wall import Wall
from games.bubbles.world_specs import WORLD_SPECS
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)



class World:
  def __init__(self, 
               outer_radius : float, 
               inner_radius : float, 
               seconds_until_game_over : float, 
               color : tuple[int, int, int], 
               bubbles : list[Bubble],
               walls : tuple[Wall]):
    self.outer_radius : float= outer_radius
    self.inner_radius : float= inner_radius
    self.seconds_until_game_over : float = seconds_until_game_over
    self.color : tuple[int, int, int] = color
    self.bubbles : list[Bubble] = bubbles
    self.walls : tuple[Wall] = walls

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


def create_world_from_level(level : int) -> World:
  spec = WORLD_SPECS[level]
  return World(
    inner_radius=spec.inner_radius,
    outer_radius=spec.outer_radius,
    seconds_until_game_over=spec.seconds_until_game_over,
    color=spec.color,
    bubbles=[bs.to_bubble() for bs in spec.bubble_specs],
    walls=spec.walls
  )