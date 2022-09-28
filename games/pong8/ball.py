import random
import pygame
import math

from games.pong8.player import Player

class Ball:

  RADIUS = 3

  def __init__(self, x : float, y : float, speed : float):
    self.x : float = x
    self.y : float = y
    self.speed : float = speed
    self.forwardAngleRadians : float = random.uniform(0, 2 * math.pi)

  def update(self, deltaTime : float, players : list[Player]):
    forwardVectorX = math.cos(self.forwardAngleRadians)
    forwardVectorY = math.sin(self.forwardAngleRadians)
    nextx = self.x + forwardVectorX * deltaTime * self.speed
    nexty = self.y + forwardVectorY * deltaTime * self.speed
    for player in players:
      hitResult = player.collissionTest(self.x, self.y, nextx, nexty)
      if hitResult:
        self.bounceOffPlayer(player)
  
  def bounceOffPlayer(self, player: Player):
    pass

  def draw(self, surface):
    pygame.draw.circle(surface, [255, 255, 255], (self.x, self.y), Ball.RADIUS)
    