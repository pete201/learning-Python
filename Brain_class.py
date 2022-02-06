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
        self.filename = playername + '.dat'                                   # each instance has a separate storage file
        try: 
            # TODO consider doing a sanity check on file (e.g. sizeof) to ensure it's what we expect
            print('Brain.init: found file ', self.filename)
            self.f = open(self.filename, 'rb')
            # read in Brain dictionary from file
            self.permDictionary = json.load(self.f)
            self.f.close()
            #print(f'Brain.init loaded dictionary: {filename} \n')
        except:
            print(f'file "{self.filename}" not found')
            print('Brain.init: building permDictionary')
            # create a new empty brain dictionary,
            self.permDictionary = self.GetPermutations()
            #print(self.permDictionary)
            print(f'length of dictionary is', len(self.permDictionary))
            print('number of boxes is:',sum(len(v) for v in self.permDictionary.values()))
            # store dictionary into 'filename'
            self.f = open(self.filename, 'w')
            json.dump(self.permDictionary, self.f)
            self.f.close()
            print(f'Brain.init: file {self.filename} created')


    def Permutate(self,stacks, tiles):
        '''takes 2 strings; stacks and tiles, and returns permutations by adding each tile to each stack'''
    
        permList = []
        for stack in stacks:
            availableTiles = tiles[:] # create a copy of 'tiles' so we don't corrupt original list
            # first remove tiles that are in stack (i.e. remove tiles already used)
            for item in stack:
                availableTiles.remove(item)

            #print(f'permutate: working on stack {stack} and tiles {availabletiles}')
            # now we have our available tiles, add each one to each stack
            for tile in availableTiles:
                
                permListItem = stack + tile
                #print(f'permutate: stack = {stack}, tile = {tile}, permListItem = {permListItem}  \n')
                permList.append(permListItem)

        return permList


    def GetPermutations(self):
        '''Creates a dictionary of game move permutations'''
        permutations = {}                   # this is the main dictionary that will be built up
        myStacks = ['']                      # initial condition for stacks

        # NOTE 9 permutations results in 986,409 memory boxes and slows down everything
        # since the last move can only occupy one square anyway, i have chosen to do only 8 itterations
        # which means that 'best_move' will have to be aware of this  
        for n in range (len(Brain.ticTacToeGrid)-1): # NOTE -1 reduces boxes from 986,409 to 623,529
        #for n in range (len(Brain.ticTacToeGrid)):
            # a 'stack' is the set of move permutations so far.  e.g. [2,5] represents top middle, then centre tiles
            #Sprint(f'this is move {n}, len(stack)={len(mystacks[0])}, len(Brain.ticTacToeGrid)={len(Brain.ticTacToeGrid)} and stacks={mystacks} \n')
            myStacks = self.Permutate(myStacks, Brain.ticTacToeGrid)
            permutations[n] = dict.fromkeys(myStacks, 0) # popluate each permutation with the initial value of 0

        return permutations


    def LearnMoves(self, moveList):
        '''input moveList, fill in AI dictionary based on winning moves'''
        # learn from game_result - (if 9 moves in game, don't try to write to last move as it won't exist in dictionary)
        print('Brain.LearnMoves: ', moveList)
        # starting at winning move, result is +1, -1, +1, -1... until end
        winningMoveScore = 1
        losingMoveScore = -1
        score = winningMoveScore

        while len(moveList) > 0:
            print(f'move {moveList[-1]} scores {score}')
            # populate AI dictionary with move:score
            self.permDictionary[str(len(moveList)-1)][str(''.join(moveList))] = score
            print(len(moveList)-1, ''.join(moveList))
            print(self.permDictionary[str(len(moveList)-1)][str(''.join(moveList))])

            moveList.pop()          # remove the last item
            if score == winningMoveScore:
                score = losingMoveScore
            else:
                score = winningMoveScore

        # now save the updated dictionary to file:
        self.f = open(self.filename, 'w')
        json.dump(self.permDictionary, self.f)
        self.f.close()
        print(f'Brain.LearnMoves: file {self.filename} updated')
        

    # TODO get best_move from brain (only 1st 8 moves in game: no suggestion for last move since only 1 square left anyway)
    #      looks up highest number from sorted (https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/?ref=rp) list given stack (game moves so far) 
    #   thinking it best to change dictionary to deep nested as it's hard to look up next move in current format
    #   think it will be easier to refernce for next move if it is
    # 1
    #   2
    #       3
    #   3
    #       2 
    # 2
    #   1
    #       3
    #   3
    #       1 
    # 3
    #   1
    #       2
    #   2
    #       1 
 
    
    # TODO destructor: __del__ make sure files are closed before exiting - beware not to break default action

def main():
    p1 = Brain('player1')

    # write a get_best_move method that looks up highest number from sorted list given stack (game moves so far)
    #print(p1[0])


    print('done')

if __name__ == '__main__':
    main()