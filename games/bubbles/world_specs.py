from games.bubbles.bubble import Bubble, BubbleType
from games.bubbles.wall import Wall
import math


class WorldSpec:
  def __init__(self, 
      outer_radius : int, 
      inner_radius : int, 
      color: tuple[int, int, int], 
      seconds_until_game_over : float,
      bubbles : tuple[Bubble],
      walls : tuple[Wall] = []):
    self.outer_radius : int = outer_radius
    self.inner_radius : int = inner_radius
    self.seconds_until_game_over : int = seconds_until_game_over
    self.color: tuple[int, int, int] = color
    self.bubbles : tuple[Bubble] = bubbles
    self.walls : tuple[Wall] = walls


WORLD_SPECS = {
  1:
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.TINY_NORMAL)
             ],
             walls = []),
  2: 
  WorldSpec(outer_radius = 300, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = math.pi * 2  * 0 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 9, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2  * 1 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 9, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2  * 2 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 9, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2  * 3 / 4, start_radius = 200, tangential_velocity = math.pi * 2 / 9, type = BubbleType.SMALL_NORMAL),
             ],
             walls = []),
  3:
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = 0, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL)
             ],
             walls = [
              Wall(angle = math.pi / 2, start_radius = 100, end_radius=500),
              Wall(angle = math.pi * 2 * 3 / 4, start_radius = 100, end_radius=500)
             ]),
  4:
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = math.pi * 2 * 5 / 8, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2 * 7 / 8, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle =math.pi * 2 * 2 / 8, start_radius = 220, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
             ],
             walls = [
              Wall(angle = math.pi * 2 * 1 / 8, start_radius = 100, end_radius=500),
              Wall(angle = math.pi * 2 * 3 / 8, start_radius = 100, end_radius=500)
             ]),
  5:
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle =math.pi * 2 * 0 / 8, start_radius = 220, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
              Bubble(start_angle =math.pi * 2 * 2 / 8, start_radius = 220, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
              Bubble(start_angle =math.pi * 2 * 4 / 8, start_radius = 220, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES),
              Bubble(start_angle =math.pi * 2 * 6 / 8, start_radius = 220, tangential_velocity = math.pi * 2 / 16, type = BubbleType.FOUR_TINIES)
             ],
             walls = [
              Wall(angle = math.pi * 2 * 1 / 8, start_radius = 100, end_radius=500),
              Wall(angle = math.pi * 2 * 3 / 8, start_radius = 100, end_radius=500),
              Wall(angle = math.pi * 2 * 5 / 8, start_radius = 100, end_radius=500),
              Wall(angle = math.pi * 2 * 7 / 8, start_radius = 100, end_radius=500),
             ]),

  6: 
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = math.pi * 2  * 0 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2  * 2 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2  * 4 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
             ],
             walls = []),
  7: 
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = 0, start_radius = 150, tangential_velocity = math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = 0, start_radius = 200, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = 0, start_radius = 250, tangential_velocity = math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = 0, start_radius = 300, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = 0, start_radius = 350, tangential_velocity = math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = 0, start_radius = 400, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
             ],
             walls = []),
  8: 
  WorldSpec(outer_radius = 400, 
             inner_radius = 250, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = math.pi * 2 * 2 / 32, start_radius = 300, tangential_velocity = math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 3 / 32, start_radius = 300, tangential_velocity = math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 4 / 32, start_radius = 300, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 5 / 32, start_radius = 300, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 6 / 32, start_radius = 300, tangential_velocity = math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 10 / 32, start_radius = 300, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 11 / 32, start_radius = 300, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 12 / 32, start_radius = 300, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 13 / 32, start_radius = 300, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
              Bubble(start_angle = math.pi * 2 * 14 / 32, start_radius = 300, tangential_velocity = math.pi * 2 / 16, type = BubbleType.SMALL_NORMAL),
             ],
             walls = [
              Wall(angle = math.pi * 2 * 0 / 16, start_radius=250, end_radius=400),
              Wall(angle = math.pi * 2 * 4 / 16, start_radius=250, end_radius=400),
              Wall(angle = math.pi * 2 * 8 / 16, start_radius=250, end_radius=400),
             ]),
  9: 
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = math.pi * 2 * 1 / 8, start_radius = 300, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2 * 3 / 8, start_radius = 200, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.EIGHT_TINIES),
              Bubble(start_angle = math.pi * 2 * 5 / 8, start_radius = 300, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2 * 7 / 8, start_radius = 200, tangential_velocity = -math.pi * 2 / 16, type = BubbleType.EIGHT_TINIES),
             ],
             walls = []),
  10: 
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubbles = [
              Bubble(start_angle = math.pi * 2  * 0 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2  * 2 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2  * 4 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 16, type = BubbleType.BIG_NORMAL),
              Bubble(start_angle = math.pi * 2  * 1 / 6, start_radius = 300, tangential_velocity = math.pi * 2 / 9, type = BubbleType.TINY_NORMAL),
              Bubble(start_angle = math.pi * 2  * 1 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 9, type = BubbleType.TINY_NORMAL),
              Bubble(start_angle = math.pi * 2  * 3 / 6, start_radius = 300, tangential_velocity = math.pi * 2 / 9, type = BubbleType.TINY_NORMAL),
              Bubble(start_angle = math.pi * 2  * 3 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 9, type = BubbleType.TINY_NORMAL),
              Bubble(start_angle = math.pi * 2  * 5 / 6, start_radius = 300, tangential_velocity = math.pi * 2 / 9, type = BubbleType.TINY_NORMAL),
              Bubble(start_angle = math.pi * 2  * 5 / 6, start_radius = 200, tangential_velocity = math.pi * 2 / 9, type = BubbleType.TINY_NORMAL),
             ],
             walls = [])
}