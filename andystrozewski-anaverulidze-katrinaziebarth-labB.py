"""
Andy Strozewski, Ana Verulidze, and Katrina Ziebarth
CS 365 Lab B
andystrozewski-anaverulidze-katrinaziebarth-labB.py
"""

import os
import copy
import random

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

def utility_evasive(boardState, player):
    numPieces = 0
    for value in boardState.getPieceLocations().values():
        if value == player:
            numPieces += 1
    return numPieces + random.random()

def utility_conquerer(boardState, player):
    numOppPieces = 0
    for value in boardState.getPieceLocations().values():
        if value != player:
            numOppPieces += 1
    return 0 - numOppPieces + random.random()

class Node:
    def __init__(self, action, boardState, depth):
        self.children = []
        self.action = action
        self.boardState = boardState
        self.depth = depth
        self.utility = None

def recursive_traversal(root, maxDepth):
    if not root.utility:
        if root.depth % 2 == 0:
            maxValue = 0
            for child in root.children:
                childUtility = recursive_traversal(child, maxDepth)
                print(root.depth + 1)
                print("Child Utility: " + str(childUtility))
                print("MaxValue: " + str(maxValue))
                if childUtility > maxValue:
                    maxValue = childUtility
                    print("MaxValue: " + str(maxValue))
            root.utility = maxValue
        else:
            minValue = float('inf')
            for child in root.children:
                childUtility = recursive_traversal(child, maxDepth)
                #print("Child Utility: " + str(childUtility))
                #print("MinValue: " + str(minValue))
                if childUtility < minValue:
                    minValue = childUtility
                    #print("MinValue: " + str(minValue))
            root.utility = minValue
    return root.utility
                    
def return_desirable_move(boardState, player):
    currDepth = 0
    maxDepth = 3
    stack = []
    root = Node(None, boardState, 0)
    currNode = root
    while currNode.depth < maxDepth:
        currDepth = currNode.depth
        for move in generate_moves(currNode.boardState, player):
            newState = transition(currNode.boardState, player, move)
            newNode = Node(move, newState, currDepth+1)
            stack.append(newNode)
            currNode.children.append(newNode)
            if newNode.depth == maxDepth:
                newNode.utility = utility_evasive(newNode.boardState, player)
        currNode = stack.pop()
    rootUtility = recursive_traversal(root, maxDepth)
    for child in root.children:
        print(child.utility)
        if child.utility == rootUtility:
            return child.action
    
def main(numRows, numCols, pieces):
    state = initial_state(numRows, numCols, pieces)
    print(return_desirable_move(state, "O"))
    """
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
    """
        
if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description='Breakthrough')
        parser.add_argument('-r', '--rows', type = int, required = True)
        parser.add_argument('-c', '--cols', type = int, required = True)
        parser.add_argument('-p', '--pieces' , type = int, required = True)
        args = parser.parse_args()
        main(args.rows, args.cols, args.pieces)
