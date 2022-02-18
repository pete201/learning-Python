# takes a tic tac toe game and roates or mirrors the game...
# ROTATE
#   orig    rot1    rot2    rot3
#   123     741     987     369
#   456     852     654     258
#   789     963     321     147
#
# MIRROR
#   orig    mirror
#   123     321
#   456     654
#   789     987

def Rotate(moveList):
    '''takes tic-tac-toe tile position and rotates tic-tac-toe grid once clockwise'''
    ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    rotateGrid = ['7', '4', '1', '8', '5', '2', '9', '6', '3']
    rotateList = []

    for tile in moveList:
        rotateTile = rotateGrid[ticTacToeGrid.index(tile)]
        rotateList.append(rotateTile)

    return rotateList


def Mirror(moveList):
    '''takes tic-tac-toe tile position and mirrors tic-tac-toe grid vertically'''
    ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    mirrorGrid = ['3', '2', '1', '6', '5', '4', '9', '8', '7']
    mirrorList = []

    for tile in moveList:
        mirrorTile = mirrorGrid[ticTacToeGrid.index(tile)]
        mirrorList.append(mirrorTile)

    return mirrorList

def Tranform8(moveList):
    '''8 games learnt from one with 3 rotations, mirror, another 3 rotations'''

    # rotate game
    for n in range(3):
        moveList = Rotate(moveList)
        print(moveList)

    moveList = Mirror(moveList)
    print(moveList)

    for n in range(3):
        moveList = Rotate(moveList)
        print(moveList)




def main():
    gameList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    print(Rotate(gameList))

    print()
    
    print(Mirror(gameList))

    print()
    Tranform8(gameList)


if __name__ == '__main__':
    main()