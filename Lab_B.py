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
    for r in range(inputState.getNumRows()+1):
        for c in range(inputState.getNumCols()):
            if (r,c) in inputState.getPieceLocations():
                piecesFile.write(inputState.getPieceLocations()[r,c])
            else:
                piecesFile.write(" ")
        piecesFile.write("\n")
    piecesFile.close()

def generate_moves(currState, player):  #revised code
    players = ("X", "O")
    possibleMoves = []
    for p in currState.getPieceLocations().Keys():
        if player == "X":
            newrow = p[0]+1 #movement will be south by one row
        else: #if player is O
            newrow = p[0]-1 #movement will be north by one row
        if p.value() == player:
            if (newrow, p[1]) in currState.getPieceLocations().Keys() and currState.getPieceLocations()[(newrow, p[1])] not in players: #pieces must be captured diagonally
             possibleMoves.append((p, "F"))
            elif (newrow, p[1]+1) in currState.getPieceLocations().Keys() and currState.getPieceLocations()[(newrow, p[1]+1)] != player and p[1]+1 < currState.numCols: #self.numCols
                possibleMoves.append((p, "FE"))
            elif (newrow, p[1]-1) in currState.getPieceLocations().Keys() and currState.getPieceLocations()[(newrow, p[1]-1)] != player and p[1]-1 > -1:
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
    return State(currState.numRows, currState.numCols, newLocations)
    
def main(numRows, numCols, pieces):
    state = initial_state(numRows, numCols, pieces)
    display_state(state)
    piecesFile = open("currentState.txt", 'r')
    print(piecesFile.read())
if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(description='Breakthrough')
        parser.add_argument('-r', '--rows', type = int, required = True)
        parser.add_argument('-c', '--cols', type = int, required = True)
        parser.add_argument('-p', '--pieces' , type = int, required = True)
        args = parser.parse_args()
        main(args.rows, args.cols, args.pieces)
