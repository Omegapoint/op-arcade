from multiprocessing.util import is_abstract_socket_namespace
import random
import pygame
import math
from games.pong8.util import projection
from games.pong8.update_results import UpdateResult

from games.pong8.player import Player

class Ball:

  RADIUS = 3
  ACCELERATION = 10

  def __init__(self, x : float, y : float, speed : float):
    self.x : float = x
    self.y : float = y
    self.speed : float = speed
    self.forwardAngleRadians : float = random.uniform(0, 2 * math.pi)

  def update(self, deltaTime : float, players : list[Player]) -> UpdateResult:
    self.speed += Ball.ACCELERATION * deltaTime
    forwardVectorX = math.cos(self.forwardAngleRadians)
    forwardVectorY = math.sin(self.forwardAngleRadians)
    nextx = self.x + forwardVectorX * deltaTime * self.speed
    nexty = self.y + forwardVectorY * deltaTime * self.speed
    for player in players:
      player_hit_result = player.paddleCollissionTest(self.x, self.y, nextx, nexty)
      goal_hit_result = player.goalCollissionTest(self.x, self.y, nextx, nexty)
      if player.is_alive() and player_hit_result:
        self.bounceOffPlayer(player)
        return UpdateResult.NONE
      elif player.is_alive() and goal_hit_result:
        player.lose_life()
        return UpdateResult.KILLME
      elif goal_hit_result:
        self.bounceOffPlayer(player)
        return UpdateResult.NONE

    # Fallthrough
    # This approach is slightly wrong because position will not update if code never reaches here. 
    self.x = nextx
    self.y = nexty
  
  def bounceOffPlayer(self, player: Player):
    forwardVectorX = math.cos(self.forwardAngleRadians)
    forwardVectorY = math.sin(self.forwardAngleRadians)
    normal_projectionX, normal_projectionY = projection(forwardVectorX, forwardVectorY, player.normalVectorX, player.normalVectorY)
    tangent_projectionX, tangent_projectionY = projection(forwardVectorX, forwardVectorY, player.tangentVectorX, player.tangentVectorY)
    newForwardVectorX = tangent_projectionX - normal_projectionX
    newForwardVectorY = tangent_projectionY - normal_projectionY
    self.forwardAngleRadians = math.atan2(newForwardVectorY, newForwardVectorX)

  def draw(self, surface):
    pygame.draw.circle(surface, [255, 255, 255], (self.x, self.y), Ball.RADIUS)
    