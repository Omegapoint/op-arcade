from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.game import Game

  
from games.bubbles.world import World
from games.bubbles.game_objects.player import Player
from games.bubbles.update_results import UpdateResult
import arcade_lib.arcade_inputs
import pygame
import math

class Players():

  def __init__(self, inputs : arcade_lib.arcade_inputs.ArcadeInput):
    self.inputs : arcade_lib.arcade_inputs.ArcadeInput = inputs
    self.score : int = 0
    self.players : list[Player] = []

  def add_score(self, score : int):
    self.score += int(score)

  def start_new_level(self, world : World):
    self.time_left : float = world.seconds_until_game_over
    self.players = []
    for i in [0,2,4,6]:
      self.players.append(Player((-i + 2) * (math.pi/4), [255, 255, 255], self.inputs.player_inputs[i], world))
    
  def update(self, delta_time : float, game : Game):
    self.time_left -= delta_time
    for player in self.players:
      update_result = player.update(delta_time, game)
      if update_result == UpdateResult.KILLME:
        self.players.remove(player)

  def draw(self, surface : pygame.Surface) -> None:
    for player in self.players:
      player.draw(surface)
