# Tic-Tac-Toe Game

This is a simple Tic-Tac-Toe game implemented using Python and the Tkinter library for the graphical user interface. The game allows the user to play against the computer, and it displays the results of each round and the final outcome.

## Features

- Graphical User Interface (GUI) built with Tkinter
- Randomized computer choices
- Tracks user and computer moves
- Displays the winner or a draw result
- Option to restart the game after completion

## Requirements

- Windows OS (for running the `.exe` file)
- Python 3.x (for running the script directly)
- Tkinter (usually comes pre-installed with Python)

## How to Run

### Using the Executable File

1. **Download the executable file:**
    - Download `main.exe` from the `./dist` directory or from the provided link.

2. **Navigate to the directory containing the executable:**
    - Open the command prompt and change to the directory containing `main.exe`:

    ```bash
    cd Tic-tac-toe\dist
    ```

3. **Run the executable:**
    - In the command prompt, type:

    ```bash
    main.exe
    ```

### Running from Source Code

1. **Clone the repository:**

    ```bash
    git clone https://github.com/alexkuznecov16/Tic-tac-toe.git
    ```

2. **Navigate to the directory containing the script:**

    ```bash
    cd Tic_tac_toe
    ```

3. **Run the script:**

    ```bash
    python main.py
    ```

## Game Instructions

1. **Start the Game:**
    - Click the "Start" button to begin the game.

2. **Make a Move:**
    - Click on any of the available cells to place your move (X).

3. **Game Progress:**
    - The game will alternate between the user and the computer making moves.

4. **Winning Condition:**
    - The first player to get three of their marks (X or O) in a row, column, or diagonal wins the game.

5. **Final Result:**
    - After the game ends, the final result will be displayed, showing whether you won, lost, or drew against the computer.

6. **Restart or Close:**
    - Click the "Restart" button to play again or the "Close" button to exit the game.

## Code Overview

- **main()**: Initializes the main application window and sets up the start and close buttons.
- **game(container)**: Manages the main game logic, including updating the board and checking for a winner.
- **result(container, winner)**: Handles the logic for determining the winner and displaying the final result.
- **computer_step()**: Implements the logic for the computer's move.

## Customization

- Modify the button styles, font, and text by changing the parameters in the `Button` and `Label` widgets.
- Adjust the window size and layout by modifying the grid positions and dimensions.

## Acknowledgements

- Tkinter documentation: [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Random module documentation: [Random](https://docs.python.org/3/library/random.html)

---

Feel free to fork the repository and contribute to the project by submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Enjoy the game!
