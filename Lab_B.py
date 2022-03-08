import os
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
    for i in range(numRows, numRows-pieceRows, -1):
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
def transition(currState, player):
    if player == "X":
        possibleMoves = ["S", "SE", "SW"]
        for p in currState.getPieceLocations().Keys():
            if p.value() == "X":
                if (p[0]+1, p[1]) in currState.getPieceLocations().Keys() and currState.getPieceLocations()[(p[0]+1, p[1])] != "X":
                    currState.getPieceLocations()[(p[0]+1, p[1])] == "X"
                    currState.pieceLocations().pop(p)
                elif (p[0]+1, p[1]+1) in currState.getPieceLocations().Keys() and currState.getPieceLocations()[(p[0]+1, p[1]+1)] != "X":
                    currState.getPieceLocations()[(p[0]+1, p[1]+1)] == "X"
                    currState.pieceLocations().pop(p)
                elif (p[0]+1, p[1]-1) in currState.getPieceLocations().Keys() and currState.getPieceLocations()[(p[0]+1, p[1]-1)] != "X":
                    currState.getPieceLocations()[(p[0]+1, p[1]-1)] == "X"
                    currState.pieceLocations().pop(p)
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
