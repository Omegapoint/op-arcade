import os
import pygame
from pygame.locals import K_q, K_w, K_e, K_r, K_t, K_y, K_u, K_i, K_o, K_a, K_s, K_d, K_f, K_g, K_h, K_j, K_k, K_l, K_z, K_x, K_c, K_v, K_b, K_n 


class ArcadePlayerInput:
  def __init__(self):
    self.__left_button_down : bool = False
    self.__right_button_down : bool = False
    self.__action_button_down : bool = False

  def update(self):
    self.__left_button_down = not self.__left_button_down and self.get_left_button_state()
    self.__right_button_down = not self.__right_button_down and self.get_right_button_state()
    self.__action_button_down = not self.__action_button_down and self.get_action_button_state()

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

  def update(self):
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
    if mode == "OP_ARCADE":
      joystick0 = pygame.joystick.Joystick(0)
      joystick1 = pygame.joystick.Joystick(1)
      joystick2 = pygame.joystick.Joystick(2)
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
    elif mode == "KEYBOARD":
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

  def update(self):
    for input in self.player_inputs:
      pygame.event.get()
      input.update()