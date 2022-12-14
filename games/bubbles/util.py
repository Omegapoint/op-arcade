from arcade_lib.vector2 import Vector2
from arcade_lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import math
import pygame


HALF_SCREEN_WIDTH = SCREEN_WIDTH / 2.0
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT / 2.0

def to_surface_coordinates(pos : Vector2) -> Vector2:
  result = pos + Vector2(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)
  return result

def get_centered_sprite_pos(sprite : pygame.Surface, pos: Vector2) -> Vector2:
  x, y = pos
  x -= sprite.get_width() / 2
  y -= sprite.get_height() / 2
  return Vector2(x, y)


def circle_line_segment_intersection(circle_center : Vector2, circle_radius : float, pt1 : Vector2, pt2 : Vector2, tangent_tol=1e-9) -> tuple[Vector2]:
  """ Find the points at which a circle intersects a line-segment.  This can happen at 0, 1, or 2 points.

  :param circle_center: The (x, y) location of the circle center
  :param circle_radius: The radius of the circle
  :param pt1: The (x, y) location of the first point of the segment
  :param pt2: The (x, y) location of the second point of the segment
  :param full_line: True to find intersections along full line - not just in the segment.  False will just return intersections within the segment.
  :param tangent_tol: Numerical tolerance at which we decide the intersections are close enough to consider it a tangent
  :return Sequence[Tuple[float, float]]: A list of length 0, 1, or 2, where each element is a point at which the circle intercepts a line segment.

  Note: We follow: http://mathworld.wolfram.com/Circle-LineIntersection.html
  modified from https://stackoverflow.com/a/59582674/1151424
  """

  (p1x, p1y), (p2x, p2y), (cx, cy) = pt1, pt2, circle_center
  (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
  dx, dy = (x2 - x1), (y2 - y1)
  dr = (dx ** 2 + dy ** 2)**.5
  big_d = x1 * y2 - x2 * y1
  discriminant = circle_radius ** 2 * dr ** 2 - big_d ** 2

  if discriminant < 0:  # No intersection between circle and line
    return []
  else:  # There may be 0, 1, or 2 intersections with the segment
    intersections = [
      (cx + (big_d * dy + sign * (-1 if dy < 0 else 1) * dx * discriminant**.5) / dr ** 2,
        cy + (-big_d * dx + sign * abs(dy) * discriminant**.5) / dr ** 2)
      for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
    fraction_along_segment = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in intersections]
    intersections = [pt for pt, frac in zip(intersections, fraction_along_segment) if 0 <= frac <= 1]
    if len(intersections) == 2 and abs(discriminant) <= tangent_tol:  # If line is tangent to circle, return just one point (as both intersections have same location)
      return [Vector2(intersections[0][0], intersections[0][1])]
    else:
      return [Vector2(i[0], i[1]) for i in intersections]
