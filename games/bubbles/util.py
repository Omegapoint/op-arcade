from games.bubbles.vector2 import Vector2
from arcade_lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import math


HALF_SCREEN_WIDTH = SCREEN_WIDTH / 2.0
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT / 2.0

def to_surface_coordinates(pos : Vector2):
  result = pos + Vector2(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)
  return result.x, result.y


def calc_line_segment_circle_intersections(circle_center : Vector2, circle_radius : float, line_start : Vector2, line_end : Vector2):
  # p is the circle parameter, lsp and lep is the two end of the line
  x0, y0 = (circle_center.x, circle_center.y)
  r0 = circle_radius
  x1,y1 = (line_start.x, line_start.y)
  x2,y2 = (line_end.x, line_end.y)
  if x1 == x2:
    if abs(r0) >= abs(x1 - x0):
        p1 = x1, y0 - math.sqrt(r0**2 - (x1-x0)**2)
        p2 = x1, y0 + math.sqrt(r0**2 - (x1-x0)**2)
        inp = [p1,p2]
        # select the points lie on the line segment
        inp = [p for p in inp if p[1]>=min(y1,y2) and p[1]<=max(y1,y2)]
    else:
        inp = []
  else:
    k = (y1 - y2)/(x1 - x2)
    b0 = y1 - k*x1
    a = k**2 + 1
    b = 2*k*(b0 - y0) - 2*x0
    c = (b0 - y0)**2 + x0**2 - r0**2
    delta = b**2 - 4*a*c
    if delta >= 0:
        p1x = (-b - math.sqrt(delta))/(2*a)
        p2x = (-b + math.sqrt(delta))/(2*a)
        p1y = k*x1 + b0
        p2y = k*x2 + b0
        inp = [[p1x,p1y],[p2x,p2y]]
        # select the points lie on the line segment
        inp = [p for p in inp if p[0]>=min(x1,x2) and p[0]<=max(x1,x2)]
    else:
        inp = []
  return inp