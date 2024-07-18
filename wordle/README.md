# Wordle Game

This is a console-based Wordle game implemented in Python. It offers two modes: a single word mode and a double word mode. The objective of the game is to guess the hidden word(s) within a limited number of attempts.
- Important to note that this is an old project (made 2 years ago back in 2022) which means the code isn't the best. I'll push an update to this soon with my new coding knowledge.

## Features

- Single Wordle Mode: Guess a single hidden word.
- Double Wordle Mode: Guess two hidden words simultaneously.
- Colored feedback for guesses:
  - Green: Correct letter in the correct position.
  - Yellow: Correct letter in the wrong position.
  - Gray: Incorrect letter.

## Setup

1. Ensure you have Python installed on your system.
2. Download or clone the repository.
3. Place a file named `english.txt` in the same directory as the script. This file should contain a list of valid words, one per line. If you cloned the repository, it'll be there.

## How to Play

1. Run the game script:
   ```sh
   python wordle_game.py
   ```

2. Choose the game mode:
- Input 1 for Single Wordle.
- Input 2 for Double Wordle.
- Enter your guesses. Each guess must be a 5-letter word.
- The game will provide colored feedback for each guess.

## License

This project is licensed under the [Unlicense](https://unlicense.org). See the [LICENSE](LICENSE) file for details. In summary, it means this project is under public domain and you are free to do whatever you wish to with it.

## Acknowledgements

This project is inspired by the wordle game. Special thanks to all the developers and contributors who have created similar projects and shared their knowledge.
Thank you to ChatGPT 3.5 for generating this lovely README.md file. The written code is of my own creation and has no AI influence whatsoever.