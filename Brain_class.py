# class to set up memory locations for every permutation of tic tac toe
# memory locations will be populated vlaues indicating likelihood of winning move
# if a move is a winning move, +1, if it's a losing move -1, for a draw do nothing

import json


class Brain(object):
    '''(playername) required for instance data storage\n
    creates memory for permutations of tic-tac-toe,\n
    player can ask for best_move\n
    winning games update memory'''

    # class attributes - common across all instances
    ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']   # represents the 9 spaces on tic tac toe grid
    #ticTacToeGrid = ['1', '2', '3']  # small list for testing only

    # constructor: see if file exists, if not create a new empty brain
    def __init__(self, playername):
        # instance attributes - particular to this instance
        self.logfilename = playername + '.csv'              # each instance has a game stats log file, updated in def gameStats
        self.filename = playername + '.dat'             # each instance has a separate storage file
        try: 
            # TODO consider doing a sanity check on file (e.g. sizeof) to ensure it's what we expect
            self.f = open(self.filename, 'rb')
            print('Brain.init: found file ', self.filename)
            # read in Brain dictionary from file
            self.brainDictionary = json.load(self.f)
            self.f.close()
            #print(f'Brain.init loaded dictionary: {filename} \n')
        except:
            print(f'file "{self.filename}" not found')
            print('Brain.init: building BrainDictionary')
            # create a new empty brain dictionary,
            # first establish List with initial dictionary from Grid (i.e. the suggestion values for first move)
            self.brainDictionary = [dict.fromkeys(Brain.ticTacToeGrid,0)]

            #now pass this dictionary to BuildNestedDictionary n times where n = len(GRID)-1
            for n in range (len(Brain.ticTacToeGrid)-1):
                self.brainDictionary.append(self.BuildNestedDict(self.brainDictionary[-1]))

            #print('Brain__init__: self.brainDictionary:', self.brainDictionary)
            print(f'length of dictionary is', len(self.brainDictionary))

            #TODO the below count does not work now that the overall brain is a list...
            #print('number of boxes is:',sum(len(v) for v in self.brainDictionary.values()))
            
            # store dictionary into 'filename'
            self.f = open(self.filename, 'w')
            json.dump(self.brainDictionary, self.f)
            self.f.close()
            print(f'Brain.init: file {self.filename} created')

    def gameStats(self, player, result):
        # try to open logfile to see if it exists
        try: 
            logf = open(self.logfilename, 'a') # this will create logfile if it does not already exist and append to end of file
            logEntry = str(player) + ',' + result + '\n'
            logf.write(logEntry)
            logf.close()
            print(f'file "{self.logfilename}" updated with {logEntry}')  
        except:
            print(f'file "{self.logfilename}" not found')        

    def BuildNestedDict(self, input_dict):
        returnDict = {}
        for input_key, input_value in input_dict.items():
            #print('BuildNestedDict: type(element)', type(input_value))
            if type(input_value) is dict:   # if it's a nested dictionary, then recursive call.  If not, then we work on input dictionary
                returnDict[input_key] = self.BuildNestedDict(input_value)
            else:
                # we get here if type NOT dictionary
                valsList = list(input_dict.keys())   # create a list of the keys in innermost dictionary so far
                for key in valsList: 
                    shortList = valsList[:]
                    shortList.remove(key)
                    returnDict[key] = dict.fromkeys(shortList,0) 

        #print('BuildNestedDict: returnDict:', returnDict)
        return returnDict


    def LearnMoves(self, moveList):
        '''input moveList, fill in AI dictionary based on winning moves'''
        # learn from game_result
        #print('Brain.LearnMoves: ', moveList)
        # working backwards from winning move, result is +1, -1, +1, -1... until beginning
        # so if number of moves is ODD then first move was WINNER, and if EVEN then first move was a LOSER
        # A number is even if division by 2 gives a remainder of 0.
        # If the remainder is 1, it is an odd number.
        winningMoveScore = 1
        losingMoveScore = -1
        if len(moveList)%2 ==0: 
            score = losingMoveScore
        else:
            score = winningMoveScore

        # pull prgressive dictionaries from list
        # start with dictionary at list[move_number]
        # from that pull dictionary at posn [i]
        # etc...
        for i,move in enumerate(moveList) :
            # format is [List[dict[dict]]] so [int][str][str]...
            # first we get the dictionary corresponding to the move number 
            gamePosn = self.brainDictionary[i]

            #then from this dictionary, we need to pull sucessive dictionaries
            for n in range(i):
                #print(f'looping thro dics; n={n} numMoves={i}')
                gamePosn = gamePosn[moveList[n]]


            # populate AI dictionary with move:score
            #print(f'Brain.LearnMoves; value found at {move} is {gamePosn}')
            if type(gamePosn[move]) is not dict:
                #print(f'Brain.LearnMoves; updating {move} by {score}')
                gamePosn[move] += score

                if score == winningMoveScore:
                    score = losingMoveScore
                else:
                    score = winningMoveScore

    def Save(self):
        # now save the updated dictionary to file:
        self.f = open(self.filename, 'w')
        json.dump(self.brainDictionary, self.f)
        self.f.close()
        print(f'Brain.LearnMoves: file {self.filename} updated')
        
    def SuggestMove(self, moveList):
        '''from moves so far, looks up stored results and finds higest ranking move'''
        
        print('Brain.SuggestMove: game so far', moveList)
        if moveList == []:
            print('movelist is empty')
        # format is [List[dict[dict]]] so [int][str][str]...
        # first we get the dictionary corresponding to the move number 
        gamePosn = self.brainDictionary[len(moveList)]

        for move in moveList:
            gamePosn = gamePosn[move]

        # gamePosn is now the dictionary with values for the next move.
        # look up highest number from values
        suggestion = max(gamePosn, key=gamePosn.get)
        print('my suggestion is ',suggestion)
        return suggestion
    
    def Rotate(self, moveList):
        '''takes tic-tac-toe tile position and rotates tic-tac-toe grid once clockwise'''
        ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        rotateGrid = ['7', '4', '1', '8', '5', '2', '9', '6', '3']
        rotateList = []

        for tile in moveList:
            rotateTile = rotateGrid[ticTacToeGrid.index(tile)]
            rotateList.append(rotateTile)

        return rotateList


    def Mirror(self, moveList):
        '''takes tic-tac-toe tile position and mirrors tic-tac-toe grid vertically'''
        ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        mirrorGrid = ['3', '2', '1', '6', '5', '4', '9', '8', '7']
        mirrorList = []

        for tile in moveList:
            mirrorTile = mirrorGrid[ticTacToeGrid.index(tile)]
            mirrorList.append(mirrorTile)

        return mirrorList

    def Learn8from1(self, moveList):
        '''8 games learnt from one with 3 rotations, mirror, another 3 rotations'''

        # Learn original game
        print('Learning original game:', moveList)
        self.LearnMoves(moveList)
        
        # rotate game 3 times and learn each...
        for n in range(3):
            moveList = self.Rotate(moveList)
            print('Learning game derivative:', moveList)
            self.LearnMoves(moveList)

        # mirror game and learn...
        moveList = self.Mirror(moveList)
        print('Learning game derivative:', moveList)
        self.LearnMoves(moveList)

        # rotate game another 3 times and learn each...
        for n in range(3):
            moveList = self.Rotate(moveList)
            print('Learning game derivative:', moveList)
            self.LearnMoves(moveList)


    # TODO destructor: __del__ make sure files are closed before exiting - beware not to break default action

def main():
    p1 = Brain('player1')

    # write a get_best_move method that looks up highest number from sorted list given stack (game moves so far)
    #print(p1[0])

    # TEST gamemoves.  gamemoves is a list which is passed to 'LearnMoves' which stores them in the List of Dictionaries
    gamemoves = ['1', '2', '4', '6', '7']
    p1.LearnMoves(gamemoves)

    print(p1.brainDictionary[0])                        # series
    print(p1.brainDictionary[0]['1'])                   # value
    print(p1.brainDictionary[1]['1'])                   # series
    print(p1.brainDictionary[1]['1']['2'])              # value
    print(p1.brainDictionary[2]['1']['2']['4'])
    print(p1.brainDictionary[3]['1']['2']['4']['6'])
    print(p1.brainDictionary[4]['1']['2']['4']['6']['7'])


    print('done')

if __name__ == '__main__':
    main()