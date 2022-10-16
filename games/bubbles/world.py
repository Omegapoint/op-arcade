from games.bubbles.bubble import Bubble
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
    self.time_left : float = self.props.seconds_until_game_over

  def __init_props(self, level : int):
    return WorldProps(500, 100, seconds_until_game_over = 60)

  def __init_bubbles(self, level : int):
    if level == 1:
      return [Bubble(0, 200, 100, math.pi * 2 / 16)]
    if level == 2:
      return [
        Bubble(0, 200, 100, math.pi * 2 / 16),
        Bubble(math.pi, 200, 100, math.pi * 2 / 16),
      ]
    if level == 3:
      return [
        Bubble(0, 200, 100, math.pi * 2 / 16),
        Bubble(math.pi * 2 / 3, 200, 100, math.pi * 2 / 16),
        Bubble(math.pi * 2 * 2 / 3, 200, 100, math.pi * 2 / 16),
      ]
    if level == 4:
      return [
        Bubble(0, 200, 100, math.pi * 2 / 16),
        Bubble(math.pi * 2 / 4, 200, 100, math.pi * 2 / 16),
        Bubble(math.pi * 2 * 2 / 4, 200, 100, math.pi * 2 / 16),
        Bubble(math.pi * 2 * 3 / 4, 200, 100, math.pi * 2 / 16),
      ]

  def update(self, delta_time : float):
    self.time_left -= delta_time
    for bubble in self.bubbles:
      bubble.update(delta_time, self)

  def bubble_hit(self, bubble : Bubble):
    new_size = bubble.size * 2 / 3
    self.bubbles.remove(bubble)
    if (new_size > Bubble.SMALLEST_RADIUS):
      self.bubbles.append(Bubble(start_angle=bubble.angle, start_radius=bubble.radius, size=new_size, tangential_velocity = bubble.tangential_velocity))
      self.bubbles.append(Bubble(start_angle=bubble.angle, start_radius=bubble.radius, size=new_size, tangential_velocity = -bubble.tangential_velocity))

  def draw(self, surface : pygame.Surface) -> None:
    surface.fill([255,255,255])
    self.__draw_timer(surface)
    pygame.draw.circle(surface, [100, 255, 100], tuple(to_surface_coordinates(Vector2())), self.props.inner_radius, 2)
    pygame.draw.circle(surface, [255, 100, 255], tuple(to_surface_coordinates(Vector2())), self.props.outer_radius, 2)
    for bubble in self.bubbles:
      bubble.draw(surface)

  def __draw_timer(self, surface : pygame.Surface) -> None:
    text_render = font.render(f'{self.time_left:.2f}', False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 0)))
    surface.blit(text_render, text_rect)