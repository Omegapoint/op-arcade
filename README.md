# OP-ARCADE

Write games for our arcade game and run them with this game manager!

## When creating a game
Make sure it doesn't spawn any new processes since this manager will not be able to kill them.

## To add a new game
Write a new entry in config.json describing for the os how to run the game.
Make sure you use full paths in config.json both for the executable file and any arguments.

## STRETCH GOALS
- Sanity check config.json file
- pipe stdout and stderr from the software to some file? Perhaps set err file in config?
