from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from games.bubbles.game import Game
  from games.bubbles.player import Player
  
from games.bubbles.hit_marker import HitMarker
from games.bubbles.update_results import UpdateResult
from arcade_lib.vector2 import Vector2
from games.bubbles.util import to_surface_coordinates, circle_line_segment_intersection

import pygame


class Hook:

  _SPEED = 150

  def __init__(self, angle : float, start_radius : float, player : Player):
    self.angle = angle
    self.start_radius = start_radius
    self.curr_radius = start_radius
    self.player = player

  def update(self, delta_time : float, game: Game) -> UpdateResult:
    self.curr_radius -= Hook._SPEED * delta_time
    for bubble in game.world.bubbles:
      #hits = calc_line_segment_circle_intersections(bubble.calc_pos(), bubble.size, self.calc_start_pos(), self.calc_end_pos())
      hits = circle_line_segment_intersection(bubble.calc_pos(), bubble.size, self.calc_start_pos(), self.calc_end_pos())
      if hits:
        if len(hits) == 2:
          hit = hits[0].calc_point_between(hits[1])
        else:
          hit = hits[0]
        game.register_gameobject(HitMarker(hit))
        game.world.bubble_hit(bubble)
        game.players.score += bubble.score
        return UpdateResult.KILLME
    if self.curr_radius <= game.world.props.inner_radius:
      return UpdateResult.KILLME
    return UpdateResult.NONE 


  def calc_start_pos(self) -> Vector2:
    return Vector2.from_radial(self.start_radius, self.angle)
  
  def calc_end_pos(self) -> Vector2:
    return Vector2.from_radial(self.curr_radius, self.angle)

  def draw(self, surface : pygame.Surface):
    start_pos_surf = tuple(to_surface_coordinates(self.calc_start_pos()))
    end_pos_surf = tuple(to_surface_coordinates(self.calc_end_pos()))
    pygame.draw.line(surface, [0, 0, 0], start_pos_surf, end_pos_surf, 2)
    pygame.draw.circle(surface, [255, 100, 100], end_pos_surf, 4, 2)