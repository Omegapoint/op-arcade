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

class StartScreen:
  def __init__(self, inputs : ArcadeInput, game : Game):
    self.inputs = inputs
    self.game : Game = game # Tight coupling buy eh whatever

  def update(self, delta_time : float) -> UpdateResult:
    if self.inputs.player_inputs[0].get_left_button_down():
      self.game.current_level = max(self.game.current_level - 1, 1)
    elif self.inputs.player_inputs[0].get_right_button_down():
      self.game.current_level = min(self.game.current_level + 1, 10)
    elif self.inputs.get_start_button_state():
      return UpdateResult.DONE
    return UpdateResult.NONE

  def draw(self, surface : pygame.Surface):

    surface.fill([200,200,200])

    bubbelt_text_render = font.render("BUBBELT", False, [0, 0, 0])
    bubbelt_text_rect = bubbelt_text_render.get_rect()
    bubbelt_text_rect.center = tuple(to_surface_coordinates(Vector2(0, -20)))
    surface.blit(bubbelt_text_render, bubbelt_text_rect)

    trubbel_text_render = font.render("TRUBBEL", False, [0, 0, 0])
    trubbel_text_rect = trubbel_text_render.get_rect()
    trubbel_text_rect.center = tuple(to_surface_coordinates(Vector2(0, 20)))
    surface.blit(trubbel_text_render, trubbel_text_rect)


    trubbel_text_render = font.render(f"Starta från bana {self.game.current_level}", False, [0, 0, 0])
    trubbel_text_rect = trubbel_text_render.get_rect()
    trubbel_text_rect.center = tuple(to_surface_coordinates(Vector2(0, 100)))
    surface.blit(trubbel_text_render, trubbel_text_rect)

    trubbel_text_render = font.render("Tryck start för att starta!", False, [0, 0, 0])
    trubbel_text_rect = trubbel_text_render.get_rect()
    trubbel_text_rect.center = tuple(to_surface_coordinates(Vector2(0, 200)))
    surface.blit(trubbel_text_render, trubbel_text_rect)
