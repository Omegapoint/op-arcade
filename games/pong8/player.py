from typing import Union
import arcade_lib.arcade_inputs
import pygame
from arcade_lib.constants import SCREEN_HEIGHT, SCREEN_WIDTH
import math
from games.pong8.util import intersectionTest

class Player:

  SPEED = 100
  MAX_POS_DIFF = 100
  HALF_SIZE = 25
  WIDTH = 4

  def __init__(self, inputs : arcade_lib.arcade_inputs.ArcadePlayerInput, startx : float, starty: float, angleRadians: float):
    self.inputs : arcade_lib.arcade_inputs.ArcadePlayerInput = inputs
    self.startx = startx
    self.starty = starty
    self.pos = 0
    self.forwardVectorX = math.cos(angleRadians)
    self.forwardVectorY = math.sin(angleRadians)

  def update(self, deltaTime: float) -> None:
    if self.inputs.get_left_button_state():
      self.pos = max(self.pos - (Player.SPEED * deltaTime), self.pos - Player.MAX_POS_DIFF)
    if self.inputs.get_right_button_state():
      self.pos = min(self.pos + (Player.SPEED * deltaTime), self.pos + Player.MAX_POS_DIFF)

  def draw(self, surface : pygame.Surface) -> None:
    xfrom = self.startx + self.forwardVectorX * (Player.HALF_SIZE + self.pos) 
    yfrom = self.starty + self.forwardVectorY * (Player.HALF_SIZE + self.pos)
    xto = self.startx - self.forwardVectorX * (Player.HALF_SIZE - self.pos) 
    yto = self.starty - self.forwardVectorY * (Player.HALF_SIZE - self.pos)
    pygame.draw.line(surface, [255, 255, 255], (xfrom, yfrom), (xto, yto), Player.WIDTH)

  def collissionTest(self, other_xfrom, other_yfrom, other_xto, other_yto) -> Union[None, tuple[float, float]]:
    xfrom = self.pos + self.forwardVectorX * Player.HALF_SIZE
    yfrom = self.pos + self.forwardVectorY * Player.HALF_SIZE
    xto = self.pos - self.forwardVectorX * Player.HALF_SIZE
    yto = self.pos - self.forwardVectorY * Player.HALF_SIZE
    p1 = (other_xfrom, other_yfrom)
    p2 = (other_xto, other_yto)
    p3 = (xfrom, yfrom)
    p4 = (xto, yto)
    return intersectionTest(p1, p2, p3, p4)

