import arcade_lib.arcade_inputs
import pygame
from arcade_lib.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Player:

  SPEED = 100

  def __init__(self, color, inputs : arcade_lib.arcade_inputs.ArcadePlayerInput, x: float, y: float):
    self.color = color
    self.inputs : arcade_lib.arcade_inputs.ArcadePlayerInput = inputs
    self.x = x
    self.y = y

  def update(self, deltaTimeSeconds: float):
    if self.inputs.get_left_button_state():
      self.x = (self.x - (Player.SPEED * deltaTimeSeconds)) % SCREEN_WIDTH
    if self.inputs.get_right_button_state():
      self.x = (self.x + (Player.SPEED * deltaTimeSeconds)) % SCREEN_WIDTH
    if self.inputs.get_action_button_state():
      self.y = (self.y - (Player.SPEED * deltaTimeSeconds)) % SCREEN_HEIGHT

  def draw(self, surface : pygame.Surface):
    pygame.draw.rect(surface, self.color, [self.x, self.y, 40, 40])