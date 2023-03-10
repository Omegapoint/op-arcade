# OP-ARCADE

Write games for our arcade game and run them with this game manager!

## When creating a game
Make sure it doesn't spawn any new processes since this manager will not be able to kill them.

## To add a new game
Write a new entry in config.json describing for the specific os how to run the game.
Make sure you use full paths in config.json both for the executable file and any arguments.
The manager uses subprocess.Popen(). Read more:
https://docs.python.org/3/library/subprocess.html#subprocess.Popen

## Run in dev mode or in arcade mode
If you set the environment variable
`OP_ARCADE=Y`
Then the game manager switches to "arcade mode" expecting input from joysticks as set up on the arcade table. The manager will also read which games to load from the `config.json` file.
If you do not set this variable, the game manager expects input from your keyboard and reads  `config_dev.json` instead.

## STRETCH GOALS
- Sanity check config.json file
- GPIO inputs
- Do something intelligent if process crashes
