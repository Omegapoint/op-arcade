from typing import Union
import arcade_lib.arcade_inputs
import pygame
from arcade_lib.constants import SCREEN_HEIGHT, SCREEN_WIDTH
import math
from games.pong8.util import intersectionTest

class Player:

  SPEED = 100
  MAX_POS_DIFF = 165
  HALF_SIZE = 25
  PADDLE_WIDTH = 4
  GOAL_WIDTH = 1
  DIST_FROM_CENTER = 400
  GOAL_DIST_FROM_CENTER = 450
  GOAL_SIZE = 200

  def __init__(self, inputs : arcade_lib.arcade_inputs.ArcadePlayerInput, tangentAngleRadians: float):
    self.inputs : arcade_lib.arcade_inputs.ArcadePlayerInput = inputs
    self.paddle_startx = (SCREEN_WIDTH / 2) + math.cos(tangentAngleRadians) * Player.DIST_FROM_CENTER
    self.paddle_starty = (SCREEN_HEIGHT / 2) + math.sin(tangentAngleRadians) * Player.DIST_FROM_CENTER
    self.goal_startx = (SCREEN_WIDTH / 2) + math.cos(tangentAngleRadians) * Player.GOAL_DIST_FROM_CENTER
    self.goal_starty = (SCREEN_HEIGHT / 2) + math.sin(tangentAngleRadians) * Player.GOAL_DIST_FROM_CENTER
    self.paddle_pos = 0
    self.tangentVectorX = math.cos(tangentAngleRadians)
    self.tangentVectorY = math.sin(tangentAngleRadians)
    self.forwardVectorX = math.cos(tangentAngleRadians + (math.pi / 2))
    self.forwardVectorY = math.sin(tangentAngleRadians + (math.pi / 2))

  def update(self, deltaTime: float) -> None:
    if self.inputs.get_left_button_state():
      self.paddle_pos = max(self.paddle_pos - (Player.SPEED * deltaTime), -Player.MAX_POS_DIFF)
    if self.inputs.get_right_button_state():
      self.paddle_pos = min(self.paddle_pos + (Player.SPEED * deltaTime), Player.MAX_POS_DIFF)

  def draw(self, surface : pygame.Surface) -> None:
    paddle_xfrom, paddle_yfrom, paddle_xto, paddle_yto = self.calc_paddle_points()
    pygame.draw.line(surface, [255, 255, 255], (paddle_xfrom, paddle_yfrom), (paddle_xto, paddle_yto), Player.PADDLE_WIDTH)
    goal_xfrom, goal_yfrom, goal_xto, goal_yto = self.calc_goal_points()
    pygame.draw.line(surface, [255, 255, 255], (goal_xfrom, goal_yfrom), (goal_xto, goal_yto), Player.GOAL_WIDTH)

  def collissionTest(self, other_xfrom, other_yfrom, other_xto, other_yto) -> Union[None, tuple[float, float]]:
    xfrom, yfrom, xto, yto = self.calc_paddle_points()
    p1 = (other_xfrom, other_yfrom)
    p2 = (other_xto, other_yto)
    p3 = (xfrom, yfrom)
    p4 = (xto, yto)
    return intersectionTest(p1, p2, p3, p4)

  def calc_paddle_points(self):
    xfrom = self.paddle_startx + self.forwardVectorX * (Player.HALF_SIZE + self.paddle_pos) 
    yfrom = self.paddle_starty + self.forwardVectorY * (Player.HALF_SIZE + self.paddle_pos)
    xto = self.paddle_startx - self.forwardVectorX * (Player.HALF_SIZE - self.paddle_pos) 
    yto = self.paddle_starty - self.forwardVectorY * (Player.HALF_SIZE - self.paddle_pos)
    return xfrom, yfrom, xto, yto

  def calc_goal_points(self):
    xfrom = self.goal_startx + self.forwardVectorX * Player.GOAL_SIZE
    yfrom = self.goal_starty + self.forwardVectorY * Player.GOAL_SIZE
    xto = self.goal_startx - self.forwardVectorX * Player.GOAL_SIZE
    yto = self.goal_starty - self.forwardVectorY * Player.GOAL_SIZE
    return xfrom, yfrom, xto, yto