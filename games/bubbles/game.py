from enum import Enum
from games.bubbles.game_object import GameObject
from games.bubbles.player import Player
from games.bubbles.bubble import Bubble
from games.bubbles.hook import Hook
from arcade_lib.arcade_inputs import ArcadeInput
import os
import math
import pygame
from games.bubbles.ready_countdown import ReadyCountdown
from games.bubbles.start_screen import StartScreen

from games.bubbles.world import World
from games.bubbles.update_results import UpdateResult

class GameState(Enum):
  START_SCREEN = 0
  READY_SCREEN = 1
  GAME_SCREEN = 2
  GAME_OVER_SCREEN = 3


class Game:
  def __init__(self, inputs : ArcadeInput, start_from_level = 1):
    self.inputs : ArcadeInput= inputs
    self.players : list[Player] = []
    self.hooks : list[Hook] = []
    self.world : World = None
    self.game_objects : list[GameObject] = []
    self.ready_countdown : ReadyCountdown = None
    self.current_level = start_from_level
    self.start_level(start_from_level)
    self.start_screen : StartScreen = StartScreen(self.inputs, self)
    self.state : GameState = GameState.START_SCREEN

  def start_level(self, level: int) -> None:
    self.current_level = level
    self.world = World(level)
    self.players = []
    self.game_objects = []
    for i in range(8):
      self.players.append(Player((-i + 2) * 45, [255, 255, 255], self.inputs.player_inputs[i], self.world.props))
    self.hooks = []
    self.ready_countdown = ReadyCountdown()
    self.state = GameState.READY_SCREEN

  def register_gameobject(self, game_object : GameObject):
    self.game_objects.append(game_object)

  def destroy_gameobject(self, game_object : GameObject):
    self.game_objects.remove(game_object)

  def register_hook(self, hook: Hook):
    self.hooks.append(hook)

  def unregister_hook(self, hook: Hook):
    self.hooks.remove(hook)

  def update(self, delta_time : float):
    self.inputs.update()
    if self.state == GameState.START_SCREEN:
      if self.start_screen.update(delta_time) == UpdateResult.DONE:
        self.start_level(self.current_level)
    if self.state == GameState.READY_SCREEN:
      if self.ready_countdown.update(delta_time) == UpdateResult.DONE:
        self.state = GameState.GAME_SCREEN
    if self.state == GameState.GAME_SCREEN:
      for game_object in self.game_objects:
        game_object.update(delta_time, self)
      for player in self.players:
        update_result = player.update(delta_time, self)
        if update_result == UpdateResult.KILLME:
          self.players.remove(player)
      self.world.update(delta_time)
      for hook in self.hooks:
        update_result = hook.update(delta_time, self)
        if update_result == UpdateResult.KILLME:
          self.unregister_hook(hook)
          hook.player.hook = None
      if len(self.world.bubbles) == 0:
        self.start_level(self.current_level + 1)


  def draw(self, surface : pygame.Surface):
    if self.state == GameState.START_SCREEN:
      self.start_screen.draw(surface)
    
    if self.state == GameState.READY_SCREEN or self.state == GameState.GAME_SCREEN:
      self.world.draw(surface)
      for game_object in self.game_objects:
        game_object.draw(surface)
      for player in self.players:
        player.draw(surface)
      for hook in self.hooks:
        hook.draw(surface)

    if self.state == GameState.READY_SCREEN:
      self.ready_countdown.draw(surface)
