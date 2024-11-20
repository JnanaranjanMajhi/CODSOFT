# CODSOFT
# 1. Simple Calculator in Python

This is a simple calculator program that performs basic arithmetic operations like addition, subtraction, multiplication, and division. The program is written in Python and allows users to interactively choose an operation and input numbers for calculation.

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first number.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second number (handles division by zero).

## How to Use

1. Clone or download the repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/calculator.git
    ```

2. Open a terminal or command prompt in the project directory.

3. Run the program by executing the following command:

    ```bash
    python calculator.py
    ```

4. Select an operation by entering the corresponding number:
   - `1` for Addition
   - `2` for Subtraction
   - `3` for Multiplication
   - `4` for Division

5. Enter two numbers for the operation.

6. The result will be displayed, and you will be asked if you want to perform another calculation.

## Code Example

Below are the main functions that handle the basic arithmetic operations:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
```
## Example Output
Here is an example of how the program runs:
Select operation:

- Addition
- Subtraction
- Multiplication
- Division Enter choice (1, 2, 3, 4): 1 Enter first number: 10 Enter second number: 5
- Addition of 10.0 and 5.0 is 15.0
- Do you want to perform another calculation? (y/n): 


# 2. Rock, Paper, Scissors Game in Python

This is a simple Rock, Paper, Scissors game written in Python where you can play against the computer. The game allows you to choose between "rock", "paper", or "scissors" and compete with the computer's randomly selected choice. The game tracks scores and lets you play multiple rounds.

## Features

- **User vs Computer**: The game allows the user to play against the computer.
- **Multiple Rounds**: You can play multiple rounds, and the game keeps track of the score.
- **Winner Announcement**: After each round, the winner is announced (either user, computer, or tie).
- **Score Tracking**: Displays current scores after every round.
- **Play Again Option**: After each round, you can choose to play again or quit the game.

## How to Use

1. Clone or download the repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/rock-paper-scissors.git
    ```

2. Open a terminal or command prompt in the project directory.

3. Run the program by executing the following command:

    ```bash
    python rock_paper_scissors.py
    ```

4. Enter your choice when prompted with "Enter your choice (rock, paper, scissors):".

5. The game will display the result of the round and show the scores.

6. After each round, you can choose to play again or quit the game.

## Example Output

Here’s an example of how the game runs:
- Enter your choice (rock, paper, scissors): rock
- You chose: rock Computer chose: paper Computer wins!
- Scores -> You: 0, Computer: 1
- Do you want to play again? (yes/no): yes
- Enter your choice (rock, paper, scissors): paper
- You chose: paper Computer chose: rock You win!
- Scores -> You: 1, Computer: 1
- Do you want to play again? (yes/no): no
- Thanks for playing! Final Scores -> You: 1 , Computer: 1

