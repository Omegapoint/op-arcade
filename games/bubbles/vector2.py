from __future__ import annotations
import math

class Vector2:
  def __init__(self, x : float = 0, y : float = 0):
    self.x : float = x
    self.y : float = y

  def rotate(self, angle: float) -> Vector2:
    raise Exception("Not implemented")

  def dot(self, other : Vector2) -> float:
    return self.x * other.x + self.y * other.y

  def __add__(self, other: Vector2) -> Vector2:
    return Vector2(self.x + other.x, self.y + other.y)

  def __sub__(self, other: Vector2) -> Vector2:
    return Vector2(self.x - other.x, self.y - other.y)  

  def multiply(self, multiplier: float) -> Vector2:
    return Vector2(self.x * multiplier, self.y * multiplier)
  
  def magnitude(self) -> float:
    return math.sqrt(self.x * self.x + self.y * self.y)

  def distance(self, other: Vector2) -> float:
    diff = self-other
    return diff.magnitude()

  def normalized(self) -> Vector2:
    magnitude_inv = 1.0 / self.magnitude()
    return self.multiply(magnitude_inv)

  @classmethod
  def from_radial(cls, radius : float, angle : float) -> Vector2:
    return Vector2(math.cos(angle), math.sin(angle)).multiply(radius)