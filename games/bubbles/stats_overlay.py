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

class StatsOverlay:
  def __init__(self, game : Game):
    self.game : Game = game # Tight coupling buy eh whatever

  def update(self, delta_time : float) -> UpdateResult:
    pass

  def draw(self, surface : pygame.Surface):
    bubbelt_text_render = font.render("BUBBELT", False, [0, 0, 0])
    bubbelt_text_rect = bubbelt_text_render.get_rect()
    bubbelt_text_rect.center = tuple(to_surface_coordinates(Vector2(-700, -20)))
    surface.blit(bubbelt_text_render, bubbelt_text_rect)

    trubbel_text_render = font.render("TRUBBEL", False, [0, 0, 0])
    trubbel_text_rect = trubbel_text_render.get_rect()
    trubbel_text_rect.center = tuple(to_surface_coordinates(Vector2(-700, 20)))
    surface.blit(trubbel_text_render, trubbel_text_rect)

    self.__draw_at_level(surface)
    self.__draw_timer(surface)

  def __draw_at_level(self, surface : pygame.Surface) -> None:
    level_text_render = font.render(f"Bana {self.game.current_level}", False, [0, 0, 0])
    level_text_rect = level_text_render.get_rect()
    level_text_rect.center = tuple(to_surface_coordinates(Vector2(700, 0)))
    surface.blit(level_text_render, level_text_rect)

  def __draw_timer(self, surface : pygame.Surface) -> None:
    text_render = font.render(f'{self.game.players.time_left:.2f}', False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 0)))
    surface.blit(text_render, text_rect)