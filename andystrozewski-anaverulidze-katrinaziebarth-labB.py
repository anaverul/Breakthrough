"""
Andy Strozewski, Ana Verulidze, and Katrina Ziebarth
CS 365 Lab B
andystrozewski-anaverulidze-katrinaziebarth-labB.py
"""

import os
import copy

class State:
    def __init__(self,rows,cols,pieceLocations):
        self.rows = rows
        self.cols = cols
        self.pieceLocations = pieceLocations
    def getPieceLocations(self):
        return self.pieceLocations
    def getNumRows(self):
        return self.rows
    def getNumCols(self):
        return self.cols
    
def initial_state(numRows, numCols, pieceRows): #pieceRows is an integer representing the number of rows each player has
    emptyRows = numRows - 2*pieceRows
    locationDict = {}
    for i in range(pieceRows):
        for j in range(numCols):
            locationDict[(i, j)] = "X"
    for i in range(numRows-1, numRows-pieceRows-1, -1):
        for j in range(numCols):
            locationDict[(i, j)] = "O"
    state = State(numRows, numCols, locationDict)
    return state
    
def display_state(inputState):
    if os.path.isfile("currentState.txt"):
        os.remove("currentState.txt")
    pieces = inputState.getPieceLocations()
    piecesFile = open("currentState.txt", 'a')
    for r in range(inputState.getNumRows()):
        for c in range(inputState.getNumCols()):
            if (r,c) in inputState.getPieceLocations():
                piecesFile.write(inputState.getPieceLocations()[r,c])
            else:
                piecesFile.write("-")
        piecesFile.write("\n")
    print("")
    piecesFile.close()

def generate_moves(currState, player):  #revised code
    players = ("X", "O")
    possibleMoves = []
    for p in currState.getPieceLocations().keys():
        if currState.getPieceLocations()[p] == player:
            if player == "X":
                newrow = p[0]+1 #movement will be south by one row
                #print(newrow)
            else: #if player is O
                newrow = p[0]-1 #movement will be north by one row
            if (newrow, p[1]) not in currState.getPieceLocations().keys(): #pieces must be captured diagonally
                possibleMoves.append((p, "F"))
            if (newrow, p[1]+1) not in currState.getPieceLocations().keys(
                    ):
                if p[1]+1 < currState.cols:
                    possibleMoves.append((p, "FE"))
            else:
                if currState.getPieceLocations()[(newrow, p[1]+1)] != player:
                    possibleMoves.append((p, "FE"))#self.numCols
            if (newrow, p[1]-1) not in currState.getPieceLocations().keys():
                if p[1]-1 > -1:
                    possibleMoves.append((p, "FW"))
            else:
                if currState.getPieceLocations()[(newrow, p[1]-1)] != player:
                    possibleMoves.append((p, "FW"))       
    return possibleMoves
    
def transition(currState, player, move):
    newLocations = copy.deepcopy(currState.getPieceLocations())
    if player == "X":
        newrow = move[0][0]+1 #movement will be south by one row
    else: #if player is O
        newrow = move[0][0]-1 #movement will be north by one row
    if move[1] == "F":
        newLocations[(newrow, move[0][1])] = player
    elif move[1] == "FE":
        newLocations[(newrow, move[0][1]+1)] = player
    else:
        newLocations[(newrow, move[0][1]-1)] = player
    newLocations.pop(move[0])
    return State(currState.rows, currState.cols, newLocations)

def isTerminal(boardState):
    terminal = False
    for key, value in boardState.getPieceLocations().items():
        if value == "X" and key[0] == boardState.getNumRows()-1:
                terminal = True
        else:
            if value == "O" and key[0] == 0:
                terminal = True
    return terminal    
    
def main(numRows, numCols, pieces):
    state = initial_state(numRows, numCols, pieces)
    display_state(state)
    piecesFile = open("currentState.txt", 'r')
    print(piecesFile.read(), end="")
    piecesFile.close()
    moves = generate_moves(state, "X")
    print("\nPossible Moves for X:")
    for move in moves:
        display_state(transition(state, "X", move))
        piecesFile = open("currentState.txt", 'r')
        print(piecesFile.read(), end="")
        piecesFile.close()
        
if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description='Breakthrough')
        parser.add_argument('-r', '--rows', type = int, required = True)
        parser.add_argument('-c', '--cols', type = int, required = True)
        parser.add_argument('-p', '--pieces' , type = int, required = True)
        args = parser.parse_args()
        main(args.rows, args.cols, args.pieces)
