# Breakthrough: Part 1
Implementation of some initial functions needed for AIs competing in a game of Breakthrough.


## Dependencies:

* **os**
* **copy**
* **random**

## How to use:

### Standard Run
* On the CLI: navigate to the directory containing Lab_B.py and type ```$python3 andystrozewski-anaverulidze-katrinaziebarth-labB.py -r 5 -c 2 -p 2 -w evasive -b defensi```. r, c and p refer to the number of rows, columns, and piece rows in that order. Make sure to replace 5, 2 and 2 with integers of choice, and evasive and defensive with heuristics of choices.

### Testing Run
* By using additional command line arguments, it is possible to specify different behavior. Adding -t test -n int to a standard command, where int is an integer, will allow you to run that number of games on the specified settings and have the resulting statistics written to statistics.txt.


### Example Output for Standard Run:

### Example Statistics for Testing Run (as seen in statistics.txt):
Total moves: 16
Number of White Pieces Captured (O): 3
Number of Black Pieces Captured (X): 2
White Heuristic: evasive
Black Heuristic: offensive
5 x 5, 1 row of pieces
White victories: 1
Black victories: 19
Total games: 20
Average Total Moves: 10.25
Average Number of White Pieces Captured: 2.05
Average Number of Black Pieces Captured: 0.15
