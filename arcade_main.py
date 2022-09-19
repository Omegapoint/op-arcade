from multiprocessing import current_process
import shlex
import subprocess
import json
import sys
import pygame

pygame.init()

class GameSpec:
  def __init__(self, title, command):
    self.title = title
    self.command = command

class GameController:
  def __init__(self, config_file_path):
    self.game_specs = []
    self.init_gamespecs(config_file_path)
    self.current_game_process = None
    self.current_game_index = 0

  def init_gamespecs(self, config_file_path):
    with open(config_file_path) as f:
      config = json.load(f)
      for game in config["games"]:
        title = game["title"]
        command = game["command"]
        # TODO: Perhaps some kind of sanity check here? Or not.
        game_spec = GameSpec(title = title, command = command)
        self.game_specs.append(game_spec)

  def start_first_game(self):
    self.start_game_from_spec(self.game_specs[self.current_game_index])
  
  def start_next_game(self):
    self.current_game_index = (self.current_game_index + 1) % len(self.game_specs)
    self.start_game_from_spec(self.game_specs[self.current_game_index])

  def start_previous_game(self):
    self.current_game_index = (self.current_game_index - 1) % len(self.game_specs)
    self.start_game_from_spec(self.game_specs[self.current_game_index])

  def stop_current_game(self):
    if self.current_game_process != None:
      print("killing current game process...")
      self.current_game_process.kill()

  # TODO: pipe stdout and stderr to somewhere
  def start_game_from_spec(self, game_spec: GameSpec):
    self.stop_current_game()
    args = shlex.split(game_spec.command)
    print(f"starting {game_spec.title}")
    print(f"args: {args}")
    self.current_game_process = subprocess.Popen(args)

if len(sys.argv) < 2:
  print("Error: specify config .json as argument")
  sys.exit()
config_file_path = sys.argv[1]

game_controller = GameController(config_file_path)

game_controller.start_first_game()

while True:
  user_input = input("n = next, p = prev, x = kill")
  if user_input == 'n':
    game_controller.start_next_game()
  elif user_input == 'p':
    game_controller.start_previous_game()
  elif user_input == 'x':
    game_controller.stop_current_game()
    exit()
  else:
    print("bad input")
