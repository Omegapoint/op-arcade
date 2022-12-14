from multiprocessing import current_process
import shlex
import subprocess
import json
import sys
import pygame
import datetime
import os
import fcntl

# This allows joystick events to be captured even without window focus
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

pygame.init()




def draw_new_text(text):
  screen.fill((0, 0, 0))
  text_surf = font.render(text, True, (255, 255, 255)) 
  screen.blit(text_surf, (100, 150))

def non_block_read(output):
  fd = output.fileno()
  fl = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
  try:
    return output.read()
  except:
    return ""

class GameSpec:
  def __init__(self, title, command):
    self.title = title
    self.command = command

class GameController:
  def __init__(self, config_file_path):
    self.game_specs = []
    self.__init_gamespecs(config_file_path)
    self.current_game_process = None
    self.current_game_spec_index = 0

  def __init_gamespecs(self, config_file_path):
    with open(config_file_path) as f:
      config = json.load(f)
      for game in config["games"]:
        title = game["title"]
        command = game["command"]
        game_spec = GameSpec(title = title, command = command)
        self.game_specs.append(game_spec)

  def start_first_game(self):
    self.start_game_from_spec(self.game_specs[self.current_game_spec_index])
  
  def start_next_game(self):
    self.current_game_spec_index = (self.current_game_spec_index + 1) % len(self.game_specs)
    self.start_game_from_spec(self.game_specs[self.current_game_spec_index])

  def start_previous_game(self):
    self.current_game_spec_index = (self.current_game_spec_index - 1) % len(self.game_specs)
    self.start_game_from_spec(self.game_specs[self.current_game_spec_index])

  def stop_current_game(self):
    if self.current_game_process != None:
      print("killing current game process...")
      self.current_game_process.kill()
      self.current_game_process.wait()
      print("Saving error log to file...")
      self.__save_err_log_to_file()

  def start_game_from_spec(self, game_spec: GameSpec):
    draw_new_text(f"Startar {game_spec.title}")
    self.stop_current_game()
    args = shlex.split(game_spec.command)
    print(f"starting {game_spec.title}")
    print(f"args: {args}")
    self.current_game_process = subprocess.Popen(args, stdout=sys.stdout, stderr=subprocess.PIPE, close_fds=False)

  def __save_err_log_to_file(self):
    if self.current_game_process != None:
      _, stderr_data = self.current_game_process.communicate()
      if len(stderr_data) > 0:
        now_string = datetime.datetime.now().strftime("%Y:%m:%dT%H:%M:%S")
        title = self.game_specs[self.current_game_spec_index].title
        err_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs", title, f'{now_string}.err')
        os.makedirs(os.path.dirname(err_file_path), exist_ok=True)
        with open(err_file_path, "wb") as err_file:
          err_file.write(stderr_data)

font = pygame.font.Font('freesansbold.ttf', 20)
size = [600, 400]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

if os.environ.get("OP_ARCADE"):
  pygame.joystick.init()
  joystick0 = pygame.joystick.Joystick(0)
  joystick0.init()
  joystick1 = pygame.joystick.Joystick(1)
  joystick1.init()
  joybutton_down = False
  game_controller = GameController(os.path.join(sys.path[0], "config.json"))
else: # dev mode
  game_controller = GameController(os.path.join(sys.path[0], "config_dev.json"))


game_controller.start_first_game()

while True:
  clock.tick(10)

  for event in pygame.event.get(): # User did something
    if event.type == pygame.QUIT: # If user clicked close
      break

  if os.environ.get("OP_ARCADE"): # Joystick input
    if joystick0.get_button(9):
      if not joybutton_down:
        game_controller.start_previous_game()
      joybutton_down = True
    elif joystick1.get_button(9):
      if not joybutton_down:
        game_controller.start_next_game()
      joybutton_down = True
    else:
      joybutton_down = False

  else: # Keyboard input
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
  
  pygame.display.flip()


