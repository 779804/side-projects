# CLI Snake Game

This is a simple console-based implementation of the classic Snake game. The game is written in Python and uses keyboard inputs to control the snake's movement. The objective is to eat food items to grow the snake while avoiding collisions with the snake's own body and the walls.

## Features

- Classic Snake gameplay.
- ASCII-based graphics.

## Requirements

- Python 3.x
- Windows OS (due to the use of `msvcrt` for capturing keyboard inputs)

## How to Play

1. **Controls:**
    - `W` - Move Up
    - `S` - Move Down
    - `A` - Move Left
    - `D` - Move Right
    - `ESC` / `X` - End game
    - `P` - Pause game

2. **Objective:**
    - Move the snake to eat the food represented by `❰❱`.
    - The snake grows longer with each food item consumed.
    - Avoid colliding with the walls or the snake's own body.

3. **Game Over:**
    - The game ends if the snake collides with the walls or its own body (loss).
    - The game ends if the snake fills the entire grid (win).

## Running the Game

1. Clone the repository:
    ```bash
    git clone --single-branch --branch snake https://github.com/779804/side-projects.git
    ```

2. Navigate to the project directory:
    ```bash
    cd side-projects
    ```

3. Run the game:
    ```bash
    python snake_game.py
    ```

## Game Settings

The game settings can be adjusted inside the game by typing 'settings' in the main menu. The current available settings are:

- `WIDTH`: Width of the game grid.
- `HEIGHT`: Height of the game grid.
- `SPEED`: Speed of the snake's movement.

## License

This project is licensed under the [Unlicense](https://unlicense.org). See the [LICENSE](LICENSE) file for details. In summary, it means this project is under public domain and you are free to do whatever you wish to with it.

## Acknowledgements

This project is inspired by the classic Snake game. Special thanks to all the developers and contributors who have created similar projects and shared their knowledge.
Thank you to ChatGPT 3.5 for generating this lovely README.md file. The written code is of my own creation and has no AI influence whatsoever.