from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.game import Game

import pygame
from arcade_lib.vector2 import Vector2
from games.bubbles.util import to_surface_coordinates, get_centered_sprite_pos
from games.bubbles.update_results import UpdateResult
from arcade_lib.arcade_inputs import ArcadeInput

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 40)

class AfterGameScreen:
  def __init__(self, inputs : ArcadeInput, game : Game):
    self.inputs = inputs
    self.game : Game = game # Tight coupling but eh whatever

  def update(self, delta_time : float) -> UpdateResult:
    if self.inputs.get_start_button_down():
      return UpdateResult.DONE
    return UpdateResult.NONE

  def draw(self, surface : pygame.Surface):

    new_surface = pygame.Surface((500, 400))
    new_surface.fill((255, 255, 255))
    new_surface.set_alpha(100)
    surface.blit(new_surface, tuple(to_surface_coordinates(get_centered_sprite_pos(new_surface, Vector2()))))

    text_render = big_font.render("Ni klarade banan!", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, -150)))
    surface.blit(text_render, text_rect)

    text_render = font.render("Bonus (level x tid):", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 40)))
    surface.blit(text_render, text_rect)

    text_render = font.render(f"{self.game.current_level} x {self.game.players.time_left:.2f} = {int(self.game.current_level*self.game.players.time_left)}", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 60)))
    surface.blit(text_render, text_rect)
    
    text_render = font.render(f"Tryck stora knappen för att fortsätta.", False, [0, 0, 0])
    text_rect = text_render.get_rect()
    text_rect.center = tuple(to_surface_coordinates(Vector2(0, 150)))
    surface.blit(text_render, text_rect)
    
