# Erik's note: modified from http://www.pygame.org/wiki/Spritesheet
from enum import Enum
import pygame

pygame.display.init()

from arcade_lib.vector2 import Vector2

class Spritesheet(object):
  def __init__(self, filename : str, sprite_width : int, sprite_height : int):
    self.sprite_width : int = sprite_width
    self.sprite_height : int = sprite_height
    try:
        self.sheet : pygame.Surface = pygame.image.load(filename).convert_alpha()
    except pygame.error as e:
        print ('Unable to load spritesheet image:', filename)
        print('error', e)
        raise SystemExit

  def image_at(self, row : int, col : int, colorkey=None):
      rect = pygame.Rect(self.sprite_width * col, self.sprite_height * row, self.sprite_width, self.sprite_height)
      image = pygame.Surface(rect.size, flags=pygame.SRCALPHA)
      image.blit(self.sheet, (0, 0), rect)
      if not colorkey:
        colorkey = image.get_at((0, 0))
      image.set_colorkey(colorkey, pygame.RLEACCEL)
      return image


class AnimationState(Enum):
  NOT_STARTED = 0,
  PLAYING = 1,
  STOPPED = 2,
  FINISHED = 3,


class SpritesheetAnimation:
  def __init__(self, spritesheet : Spritesheet, sheet_coords : list[(int, int)], fps : float, is_looping : bool = True, is_flipped : bool = False):
    "sheet coords row, col : 0-indexed"
    self.spritesheet : Spritesheet = spritesheet
    self.sheet_coords : list[(int, int)] = sheet_coords
    self.fps : float = fps
    self.is_flipped : bool = is_flipped
    self.is_looping : bool = is_looping
    self.playtime : float= 0.0
    self.state : AnimationState = AnimationState.NOT_STARTED
    
  def update(self, delta_time: float):
    if (self.state == AnimationState.PLAYING):
      self.playtime += delta_time

  def restart(self):
    self.playtime = 0.0
    self.state = AnimationState.PLAYING

  def stop(self):
    self.state = AnimationState.STOPPED

  def get_current_image(self) -> pygame.Surface:
    cycles_since_start = int(self.playtime * self.fps)
    if not self.is_looping and cycles_since_start > len(self.sheet_coords):
      current_frame = len(self.sheet_coords) -1
      if self.state == AnimationState.PLAYING:
        self.state = AnimationState.FINISHED
    else:
      current_frame = cycles_since_start % len(self.sheet_coords)
    image = self.spritesheet.image_at(self.sheet_coords[current_frame][0], self.sheet_coords[current_frame][1])
    if self.is_flipped:
      image = pygame.transform.flip(image, flip_x=True, flip_y=False)
    return image

class Animator:
  def __init__(self, animations_map : dict[Enum, SpritesheetAnimation], initial_state : Enum):
    self.animations_map : dict[Enum, SpritesheetAnimation] = animations_map
    self.state : Enum = initial_state
    self.current_animation : SpritesheetAnimation = self.animations_map[self.state]

  def set_state(self, state):
    if state != self.state:
      self.state = state
      self.current_animation = self.animations_map[self.state]
      self.current_animation.restart()

  def get_current_image(self) -> pygame.Surface:
    return self.current_animation.get_current_image()

  def update(self, delta_time : float):
    self.current_animation.update(delta_time)