import pygame
from arcade_lib.vector2 import Vector2
from games.bubbles.util import to_surface_coordinates
from games.bubbles.update_results import UpdateResult

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)

class ReadyCountdown:
  def __init__(self):
    self.seconds_left = 3

  def update(self, delta_time : float) -> UpdateResult:
    self.seconds_left -= delta_time
    if self.seconds_left < 0:
      return UpdateResult.DONE
    return UpdateResult.NONE

  def draw(self, surface : pygame.Surface):
    text = ""
    if self.seconds_left > 2:
      text = "Klara"
      pygame.draw.circle(surface, [255, 0, 0], tuple(to_surface_coordinates(Vector2())), 50, 10)
    elif self.seconds_left > 1:
      text = "Färdiga"
      pygame.draw.circle(surface, [255, 255, 0], tuple(to_surface_coordinates(Vector2())), 60, 15)
    else:
      text = "Gå!"
      pygame.draw.circle(surface, [0, 255, 0], tuple(to_surface_coordinates(Vector2())), 70, 20)
    text_render = font.render(text, False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 20)))
    surface.blit(text_render, text_rect)
