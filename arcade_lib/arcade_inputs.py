import os
import pygame
from pygame.locals import K_RETURN, K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_a, K_s, K_d, K_f, K_g, K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_v, K_b, K_n 


class ArcadePlayerInput:
  def __init__(self):
    self.__left_button_down : bool = False
    self.__right_button_down : bool = False
    self.__action_button_down : bool = False

    self.__last_frame_left_button : bool = False
    self.__last_frame_right_button : bool = False
    self.__last_frame_action_button : bool = False

  def update(self) -> None:
    self.__left_button_down = not self.__last_frame_left_button and self.get_left_button_state()
    self.__right_button_down = not self.__last_frame_right_button and self.get_right_button_state()
    self.__action_button_down = not self.__last_frame_action_button and self.get_action_button_state()
    
    self.__last_frame_left_button = self.get_left_button_state()
    self.__last_frame_right_button = self.get_right_button_state()
    self.__last_frame_action_button = self.get_action_button_state()

  def get_left_button_down(self) -> bool:
    return self.__left_button_down

  def get_right_button_down(self) -> bool:
    return self.__right_button_down

  def get_action_button_down(self) -> bool:
    return self.__action_button_down

  def get_left_button_state(self) -> bool:
    raise ("Not implemented")

  def get_right_button_state(self) -> bool:
    raise ("Not implemented")

  def get_action_button_state(self) -> bool:
    raise ("Not implemented")


class JoystickArcadePlayerInput(ArcadePlayerInput):
  def __init__(self, joystick : pygame.joystick.Joystick, left_button_id: int, right_button_id: int, action_button_id: int):
    super().__init__()
    self.joystick = joystick
    self.left_button_id = left_button_id
    self.right_button_id = right_button_id
    self.action_button_id = action_button_id

  def get_left_button_state(self) -> bool:
    return self.joystick.get_button(self.left_button_id)

  def get_right_button_state(self) -> bool:
    return self.joystick.get_button(self.right_button_id)

  def get_action_button_state(self) -> bool:
    return self.joystick.get_button(self.action_button_id)


class KeyboardArcadePlayerInput(ArcadePlayerInput):
  def __init__(self, left_button_id: int, right_button_id: int, action_button_id: int):
    super().__init__()
    self.left_button_id = left_button_id
    self.right_button_id = right_button_id
    self.action_button_id = action_button_id
    self.keys : list[int] = []

  def update(self) -> None:
    self.keys = pygame.key.get_pressed()
    super().update()

  def get_left_button_state(self) -> bool:
    return self.keys[self.left_button_id]

  def get_right_button_state(self) -> bool:
    return self.keys[self.right_button_id]

  def get_action_button_state(self) -> bool:
    return self.keys[self.action_button_id]

class ArcadeInput:
  def __init__(self, mode : str):
    self.player_inputs : list[ArcadePlayerInput] = []
    self.mode = mode
    self.start_button_joystick = None
    self.__last_frame_start_button : bool = False
    self.__start_button_down : bool = False
    if self.mode == "OP_ARCADE":
      pygame.joystick.init()
      joystick0 = pygame.joystick.Joystick(0)
      joystick1 = pygame.joystick.Joystick(1)
      joystick2 = pygame.joystick.Joystick(2)
      self.start_button_joystick = joystick0
      joystick0.init()
      joystick1.init()
      joystick2.init()
      self.player_inputs.append(JoystickArcadePlayerInput(joystick2, 6, 7, 8))
      self.player_inputs.append(JoystickArcadePlayerInput(joystick2, 9, 10, 11))
      self.player_inputs.append(JoystickArcadePlayerInput(joystick1, 7, 6, 8))
      self.player_inputs.append(JoystickArcadePlayerInput(joystick1, 4, 3, 5))
      self.player_inputs.append(JoystickArcadePlayerInput(joystick1, 1, 0, 2))
      self.player_inputs.append(JoystickArcadePlayerInput(joystick0, 1, 0, 2))
      self.player_inputs.append(JoystickArcadePlayerInput(joystick0, 3, 4, 5))
      self.player_inputs.append(JoystickArcadePlayerInput(joystick2, 3, 4, 5))
    elif self.mode == "KEYBOARD":
      self.player_inputs.append(KeyboardArcadePlayerInput(K_q, K_w, K_e))
      self.player_inputs.append(KeyboardArcadePlayerInput(K_r, K_t, K_y))
      self.player_inputs.append(KeyboardArcadePlayerInput(K_u, K_i, K_o))
      self.player_inputs.append(KeyboardArcadePlayerInput(K_a, K_s, K_d))
      self.player_inputs.append(KeyboardArcadePlayerInput(K_f, K_g, K_h))
      self.player_inputs.append(KeyboardArcadePlayerInput(K_j, K_k, K_l))
      self.player_inputs.append(KeyboardArcadePlayerInput(K_z, K_x, K_c))
      self.player_inputs.append(KeyboardArcadePlayerInput(K_v, K_b, K_n))
    else:
      raise("Invalid input mode")

  def get_start_button_state(self):
    if self.mode == "OP_ARCADE":
      return self.start_button_joystick.get_button(8)
    elif self.mode == "KEYBOARD":
      keys = pygame.key.get_pressed()
      return keys[K_RETURN]

  def get_start_button_down(self):
    return self.__start_button_down

  def update(self) -> None:
    pygame.event.get()
    self.__start_button_down = not self.__last_frame_start_button and self.get_start_button_state()
    self.__last_frame_start_button = self.get_start_button_state()
    for input in self.player_inputs:
      input.update()