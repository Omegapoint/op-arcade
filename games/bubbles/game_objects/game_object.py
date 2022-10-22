from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from games.bubbles.game import Game
import pygame

class GameObject:
  def update(self, delta_time, game : Game):
    raise("Not implemented")

  def draw(self, surface : pygame.Surface):
    raise("Not implemented")