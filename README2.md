# Part 2
Implementation of utility functions for the agents competing in a game of Breakthrough

## Dependencies:

* **os**
* **random**
* **copy**

## How to use:

* On the CLI: navigate to the Lab B folder that contains andystrozewski-anaverulidze-katrinaziebarth-labB.py, and type ```andystrozewski-anaverulidze-katrinaziebarth-labB.py -r rows -c cols -p num_pieces -w heuristic_white -b heuristic_black -t run_type -n run_num```. Make sure to replace rows, cols and num pieces with the number of rows and columns for the board as well as the number of pieces each player should have, in that order. heuristic_white and heuristic_black should be replaced with the utility functions you would like each player to use. The utility functions are as follows: conqueror, evasive, defensive, offensive.
-t and -n are optional arguments, -t indicates the run type. If it isn't passed, the command will run in the regular mode and display results for that specific game. if "test" is passed, the game will be replayed multiple times. If "steps" is passed, each move will be printed out to the screen. -n indicates the number of times the game should be played in test mode.

### example commands:
```andystrozewski-anaverulidze-katrinaziebarth-labB.py -r 5 -c 5 -p 1 -w offensive -b defensive```  
```andystrozewski-anaverulidze-katrinaziebarth-labB.py -r 5 -c 5 -p 1 -w offensive -b defensive -t test -n 20```  
```andystrozewski-anaverulidze-katrinaziebarth-labB.py -r 5 -c 5 -p 1 -w offensive -b defensive -t steps```  

### example output (for second command, showing statistics printed after output for each of the games):
```
White Heuristic: offensive  
Black Heuristic: defensive  
5 x 5, 1 row of pieces  
White victories: 4  
Black victories: 16  
Total games: 20  
Average Total Moves: 14.3  
Average Number of White Pieces Captured: 3.1  
Average Number of Black Pieces Captured: 1.3
```
