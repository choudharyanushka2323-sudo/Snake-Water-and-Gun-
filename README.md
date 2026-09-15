# Snake, Water, Gun 🐍💧🔫

A simple command-line game in Python, similar to Rock-Paper-Scissors, where you play against the computer using **Snake**, **Water**, and **Gun**.

## Rules

- 🐍 **Snake** beats 🔫 **Gun**
- 🔫 **Gun** beats 💧 **Water**
- 💧 **Water** beats 🐍 **Snake**

If both players pick the same thing, it's a draw.

## How to Play

1. Make sure you have Python installed on your system.
2. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd "Snake,Water And Gun"
   ```
3. Run the game:
   ```bash
   python main.py
   ```
4. When prompted, enter your choice:
   - `s` for Snake
   - `w` for Water
   - `g` for Gun
5. The result (win, lose, or draw) will be printed to the console.

## Example

```
Enter your choice (s = snake, w = water, g = gun): s
You Win! 😊
```

## Project Structure

```
.
├── main.py       # Main game logic
└── README.md     # Project documentation
```

## How It Works

- The computer randomly picks one of `1` (snake), `-1` (water), or `0` (gun) using Python's `random` module.
- Your input (`s`, `w`, or `g`) is mapped to the same numeric values via a dictionary.
- The two values are compared to determine the winner based on the rules above.

## Requirements

- Python 3.x (no external libraries needed — uses only the built-in `random` module)

## License

Feel free to use, modify, and share this project.
