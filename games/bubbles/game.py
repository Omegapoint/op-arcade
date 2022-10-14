from games.bubbles.player import Player
from games.bubbles.bubble import Bubble
from games.bubbles.hook import Hook
from arcade_lib.arcade_inputs import ArcadeInput, ArcadePlayerInput
import os
import math
import pygame
from games.bubbles.ready_countdown import ReadyCountdown

from games.bubbles.world import World
from games.bubbles.update_results import UpdateResult

class Game:
  def __init__(self, inputs : list[ArcadePlayerInput], start_from_level = 1):
    self.inputs : list[ArcadePlayerInput]= inputs
    self.players : list[Player] = []
    self.hooks : list[Hook] = []
    self.world : World = None
    self.ready_countdown : ReadyCountdown = None
    self.current_level = start_from_level
    self.initialize_level(start_from_level)

  def initialize_level(self, level: int) -> None:
    self.current_level = level
    self.world = World(level)
    self.players = []
    for i in range(8):
      self.players.append(Player((-i + 2) * 45, [255, 255, 255], self.inputs.player_inputs[i], self.world.props))
    self.hooks = []
    self.ready_countdown = ReadyCountdown()

  def register_hook(self, hook: Hook):
    self.hooks.append(hook)

  def unregister_hook(self, hook: Hook):
    self.hooks.remove(hook)

  def update(self, delta_time : float):
    self.inputs.update()
    if self.ready_countdown.active:
      self.ready_countdown.update(delta_time)
    else:
      for player in self.players:
        update_result = player.update(delta_time, self)
        if update_result == UpdateResult.KILLME:
          self.players.remove(player)
      self.world.update(delta_time)
      for hook in self.hooks:
        update_result = hook.update(delta_time, self.world)
        if update_result == UpdateResult.KILLME:
          self.unregister_hook(hook)
          hook.player.hook = None
      if len(self.world.bubbles) == 0:
        self.initialize_level(self.current_level + 1)


  def draw(self, surface : pygame.Surface):
    self.world.draw(surface)
    self.ready_countdown.draw(surface)
    for player in self.players:
      player.draw(surface)
    for hook in self.hooks:
      hook.draw(surface)
