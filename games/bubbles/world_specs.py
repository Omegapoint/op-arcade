
  
from enum import Enum
from games.bubbles.bubble import Bubble, BubbleType
from games.bubbles.wall import Wall
import math



class BubbleSpawnSpec:
  def __init__(self, angular_pos: float, radial_pos : float, tangential_velocity : float, bubble_type: BubbleType):
    self.angular_pos : float = angular_pos
    self.radial_pos : float = radial_pos
    self.tangential_velocity : float = tangential_velocity
    self.bubble_type : BubbleType = bubble_type

  def to_bubble(self) -> Bubble:
    return Bubble(angular_pos=self.angular_pos, 
                  radial_pos=self.radial_pos, 
                  tangential_velocity=self.tangential_velocity, 
                  type=self.bubble_type)



class WorldSpec:
  def __init__(self, 
      outer_radius : int, 
      inner_radius : int, 
      color: tuple[int, int, int], 
      seconds_until_game_over : float,
      bubble_specs : list[BubbleSpawnSpec],
      walls : tuple[Wall] = []):
    self.outer_radius : int = outer_radius
    self.inner_radius : int = inner_radius
    self.seconds_until_game_over : int = seconds_until_game_over
    self.color: tuple[int, int, int] = color
    self.bubble_specs : list[BubbleSpawnSpec] = bubble_specs
    self.walls : tuple[Wall] = walls


SPEED_NORMAL : float = math.pi * 2 / 16
SPEED_FAST : float = math.pi * 2 / 9


  

WORLD_SPECS = {
  1:
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.TINY_NORMAL)
             ],
             walls = []),
  2: 
  WorldSpec(outer_radius = 300, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 0 / 4, radial_pos = 200, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 1 / 4, radial_pos = 200, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 2 / 4, radial_pos = 200, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 3 / 4, radial_pos = 200, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.SMALL_NORMAL),
             ],
             walls = []),
  3:
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL)
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
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 5 / 8, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 7 / 8, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos =math.pi * 2 * 2 / 8, radial_pos = 220, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.FOUR_TINIES),
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
             bubble_specs = [
              BubbleSpawnSpec(angular_pos =math.pi * 2 * 0 / 8, radial_pos = 220, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.FOUR_TINIES),
              BubbleSpawnSpec(angular_pos =math.pi * 2 * 2 / 8, radial_pos = 220, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.FOUR_TINIES),
              BubbleSpawnSpec(angular_pos =math.pi * 2 * 4 / 8, radial_pos = 220, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.FOUR_TINIES),
              BubbleSpawnSpec(angular_pos =math.pi * 2 * 6 / 8, radial_pos = 220, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.FOUR_TINIES)
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
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 0 / 6, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 2 / 6, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 4 / 6, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
             ],
             walls = []),
  7: 
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 150, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 200, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 250, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 300, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 350, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = 0, radial_pos = 400, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
             ],
             walls = []),
  8: 
  WorldSpec(outer_radius = 400, 
             inner_radius = 250, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 2 / 32, radial_pos = 300, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 3 / 32, radial_pos = 300, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 4 / 32, radial_pos = 300, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 5 / 32, radial_pos = 300, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 6 / 32, radial_pos = 300, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 10 / 32, radial_pos = 300, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 11 / 32, radial_pos = 300, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 12 / 32, radial_pos = 300, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 13 / 32, radial_pos = 300, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.SMALL_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 14 / 32, radial_pos = 300, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.SMALL_NORMAL),
             ],
             walls = [
              Wall(angle = math.pi * 2 * 0 / 16, start_radius = 250, end_radius=400),
              Wall(angle = math.pi * 2 * 4 / 16, start_radius = 250, end_radius=400),
              Wall(angle = math.pi * 2 * 8 / 16, start_radius = 250, end_radius=400),
             ]),
  9: 
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 1 / 8, radial_pos = 300, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 3 / 8, radial_pos = 200, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.EIGHT_TINIES),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 5 / 8, radial_pos = 300, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2 * 7 / 8, radial_pos = 200, tangential_velocity = -math.pi * 2 / 16, bubble_type = BubbleType.EIGHT_TINIES),
             ],
             walls = []),
  10: 
  WorldSpec(outer_radius = 500, 
             inner_radius = 100, 
             color = (200, 200, 200), 
             seconds_until_game_over = 60.0, 
             bubble_specs = [
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 0 / 6, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 2 / 6, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 4 / 6, radial_pos = 200, tangential_velocity = SPEED_NORMAL, bubble_type = BubbleType.BIG_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 1 / 6, radial_pos = 300, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.TINY_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 1 / 6, radial_pos = 200, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.TINY_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 3 / 6, radial_pos = 300, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.TINY_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 3 / 6, radial_pos = 200, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.TINY_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 5 / 6, radial_pos = 300, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.TINY_NORMAL),
              BubbleSpawnSpec(angular_pos = math.pi * 2  * 5 / 6, radial_pos = 200, tangential_velocity = SPEED_FAST, bubble_type = BubbleType.TINY_NORMAL),
             ],
             walls = [])
}


