# Rock-paper-Scissors 

This Python program allows users to play a simple game of "Rock, Paper, Scissors" against the computer. This project is from 
@Freecodecamp Youtube - 12 beginner Python projects. The original projects shows if you won or lost against the computer but never shows the computer answer.
i added an ```" f string " ```to the ```"if statements"```to get the computers response.

``` Python
import random
#  random.choice(sequence) ..equired. A sequence like a list, a tuple, a range of numbers etc
def play():
    user = input("Whats youre choice? 'r' for rock, 'p' for paper, 's' for scissors:  ")

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f'It\'s a tie. MY choice, {computer}'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return f'You won!, MY choice, {computer}'

    return f'You lost. MY choice, {computer}'

def is_win(player, opponent):
    # return true if player wins
# r > s, S > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
```


## How It Works

1. User Input: The user chooses one of three options:

```'r'``` for rock
```'p' ```for paper
```'s'```for scissors

2. Computer Choice: The computer randomly selects one of the three options using the ```random.choice()``` method.

3. Determine the Winner: The program compares the user's choice with the computer's choice and determines the result:

It's a tie if both choices are the same.
The user wins if their choice beats the computer's choice (according to the game's rules).
Otherwise, the computer wins.

4. Display the Result: The result of the game, along with the computer's choice, is displayed to the user.


## Code Explanation

### Imports
```Python
import random
```
The random module is used to generate the computer's choice. The ```random.choice()``` function selects a random item from a list or sequence.

## Function Definitions

```play()```

This function handles the main game logic:

* Prompts the user to input their choice.
* Randomly generates the computer's choice.
* Determines the result by comparing the user's choice and the computer's choice.
* Returns a message indicating whether the user won, lost, or tied.

```is_win(player, opponent)```

This helper function determines if the player's choice beats the opponent's choice based on the rules of the game:

* Rock ```(r)```beats Scissors ```(s)```.
* Scissors ```(s)``` beats Paper ```(p)```.
* Paper ```(p)``` beats Rock ```(r)```.

 ## Game Logic

 ```Pyhon
if user == computer:
    return f'It\'s a tie. MY choice, {computer}'
```
f the user's choice is the same as the computer's choice, the game is a tie.

```Python
if is_win(user, computer):
    return f'You won!, MY choice, {computer}'
```
  The user wins if the is_win() function returns True.

  ```Python
return f'You lost. MY choice, {computer}'
```
If neither of the above conditions is met, the computer wins.

## Example Output
```Python
Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors: r
You won!, MY choice, s
```

## How to Run the Program

1. Copy the code into a Python file, e.g., rock_paper_scissors.py.
2. Run the file in a Python environment (e.g., terminal, IDE).
3. Follow the prompt to input your choice ('r', 'p', or 's').
4. View the result of the game.

