# OP-ARCADE

Write games for our arcade game and run them with this game manager!

## When creating a game
Make sure it doesn't spawn any new processes since this manager will not be able to kill them.

## To add a new game
Write a new entry in config.json describing for the os how to run the game.
Make sure you use full paths in config.json both for the executable file and any arguments.
The manager uses subprocess.Popen(). Read more:
https://docs.python.org/3/library/subprocess.html#subprocess.Popen

## STRETCH GOALS
- Sanity check config.json file
- GPIO inputs
- Do something intelligent if process crashes