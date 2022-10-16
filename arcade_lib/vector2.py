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

  def __mul__(self, other : float) -> Vector2:
    return Vector2(self.x * other, self.y * other)

  def __iter__(self):
    return iter((self.x, self.y))

  def magnitude(self) -> float:
    return math.sqrt(self.x * self.x + self.y * self.y)

  def distance(self, other: Vector2) -> float:
    diff = self-other
    return diff.magnitude()

  def normalized(self) -> Vector2:
    magnitude_inv = 1.0 / self.magnitude()
    return self.multiply(magnitude_inv)

  def unwrap(self) -> tuple[int, int]:
    return self.x, self.y

  def calc_point_between(self, other : Vector2) -> Vector2:
    return self + ((other - self) * 0.5)


  @classmethod
  def from_radial(cls, radius : float, angle : float) -> Vector2:
    return Vector2(math.cos(angle), math.sin(angle)) * radius