from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.game import Game

import pygame
from arcade_lib.vector2 import Vector2
from games.bubbles.util import to_surface_coordinates
from games.bubbles.update_results import UpdateResult
from arcade_lib.arcade_inputs import ArcadeInput

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)

class EndScreen:
  def __init__(self, inputs : ArcadeInput, game : Game):
    self.inputs = inputs
    self.game : Game = game # Tight coupling buy eh whatever

  def update(self, delta_time : float) -> UpdateResult:
    if self.inputs.get_start_button_down():
      return UpdateResult.DONE
    return UpdateResult.NONE

  def draw(self, surface : pygame.Surface):
    surface.fill([200,200,200])

    text_render = font.render("Spelet är över!", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, -60)))
    surface.blit(text_render, text_rect)

    text_render = font.render("Så här gick det", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, -20)))
    surface.blit(text_render, text_rect)

    text_render = font.render(f"Ni kom till bana {self.game.current_level}", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 20)))
    surface.blit(text_render, text_rect)

    text_render = font.render(f"och fick {self.game.players.score} poäng!", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 60)))
    surface.blit(text_render, text_rect)
