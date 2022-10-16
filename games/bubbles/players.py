from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.game import Game

  
from games.bubbles.world import WorldProps
from games.bubbles.player import Player
from games.bubbles.update_results import UpdateResult
import arcade_lib.arcade_inputs
import pygame

class Players():

  def __init__(self, inputs : arcade_lib.arcade_inputs.ArcadeInput, worldProps : WorldProps):
    self.inputs : arcade_lib.arcade_inputs.ArcadeInput = inputs
    self.players : list[Player] = []
    self.time_left : float = 0
    self.score : int = 0
    for i in range(8):
      self.players.append(Player((-i + 2) * 45, [255, 255, 255], self.inputs.player_inputs[i], worldProps))
    
  def update(self, delta_time : float, game : Game):
    for player in self.players:
      update_result = player.update(delta_time, game)
      if update_result == UpdateResult.KILLME:
        self.players.remove(player)

  def draw(self, surface : pygame.Surface) -> None:
    for player in self.players:
      player.draw(surface)
