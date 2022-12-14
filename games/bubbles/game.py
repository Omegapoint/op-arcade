from enum import Enum
from games.bubbles.screens.after_game_screen import AfterGameScreen
from games.bubbles.screens.end_screen import EndScreen
from games.bubbles.screens.start_screen import StartScreen
from games.bubbles.game_objects.game_object import GameObject
from games.bubbles.game_objects.hook import Hook
from arcade_lib.arcade_inputs import ArcadeInput
import pygame
from games.bubbles.players import Players
from games.bubbles.views.ready_countdown import ReadyCountdown
from games.bubbles.views.stats_overlay import StatsOverlay

from games.bubbles.world_specs import WORLD_SPECS
from games.bubbles.world import World, create_world_from_level
from games.bubbles.update_results import UpdateResult

class GameState(Enum):
  START_SCREEN = 0
  READY_SCREEN = 1
  GAME_SCREEN = 2
  AFTER_GAME_SCREEN = 3
  GAME_OVER_SCREEN = 4


class Game:
  def __init__(self, inputs : ArcadeInput):
    self.inputs : ArcadeInput= inputs
    self.hooks : list[Hook] = []
    self.world : World = None
    self.game_objects : list[GameObject] = []
    self.ready_countdown : ReadyCountdown = None
    self.current_level = 1
    self.start_screen : StartScreen = StartScreen(self.inputs, self)
    self.after_game_screen : AfterGameScreen = AfterGameScreen(self.inputs, self)
    self.end_screen : EndScreen = EndScreen(self.inputs, self)
    self.state : GameState = GameState.START_SCREEN
    self.stats_overlay : StatsOverlay = StatsOverlay(self)
    self.players : Players = Players(self.inputs)

  def start_level(self, level: int) -> None:
    self.current_level = level
    self.world = create_world_from_level(level)
    self.players.start_new_level(self.world)
    self.game_objects = []
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

  def is_on_last_level(self):
    if not (self.current_level + 1) in WORLD_SPECS:
      return True

  def update(self, delta_time : float):
    self.inputs.update()
    if self.state == GameState.START_SCREEN:
      if self.start_screen.update(delta_time) == UpdateResult.DONE:
        self.start_level(self.current_level)
    elif self.state == GameState.READY_SCREEN:
      if self.ready_countdown.update(delta_time) == UpdateResult.DONE:
        self.state = GameState.GAME_SCREEN
    elif self.state == GameState.GAME_SCREEN:
      for game_object in self.game_objects:
        game_object.update(delta_time, self)
      self.players.update(delta_time, self)
      self.world.update(delta_time)
      for hook in self.hooks:
        update_result = hook.update(delta_time, self)
        if update_result == UpdateResult.KILLME:
          self.unregister_hook(hook)
          hook.player.hook = None
      if len(self.world.bubbles) == 0:
        self.players.add_score(self.players.time_left * self.current_level)
        self.state = GameState.AFTER_GAME_SCREEN
      elif len(self.players.players) == 0 or self.players.time_left <= 0:
        self.state = GameState.GAME_OVER_SCREEN
    elif self.state == GameState.AFTER_GAME_SCREEN:
      if self.after_game_screen.update(delta_time) == UpdateResult.DONE:
        if self.is_on_last_level():
          self.state = GameState.GAME_OVER_SCREEN
        else:
          self.start_level(self.current_level + 1)
    elif self.state == GameState.GAME_OVER_SCREEN:
      if self.end_screen.update(delta_time) == UpdateResult.DONE:
        self.current_level = 1
        self.state = GameState.START_SCREEN


  def draw(self, surface : pygame.Surface):
    if self.state == GameState.START_SCREEN:
      self.start_screen.draw(surface)
    
    if self.state in (GameState.READY_SCREEN, GameState.GAME_SCREEN, GameState.AFTER_GAME_SCREEN):
      self.world.draw(surface)
      for game_object in self.game_objects:
        game_object.draw(surface)
      self.players.draw(surface)
      for hook in self.hooks:
        hook.draw(surface)
      self.stats_overlay.draw(surface)

    if self.state == GameState.READY_SCREEN:
      self.ready_countdown.draw(surface)

    if self.state == GameState.AFTER_GAME_SCREEN:
      self.after_game_screen.draw(surface)

    if self.state == GameState.GAME_OVER_SCREEN:
      self.end_screen.draw(surface)
