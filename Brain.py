# class to set up memory locations for every permutation of tic tac toe
# memory locations will be populated vlaues indicating likelihood of winning move
# if a move is a winning move, +1, if it's a losing move -1, for a draw do nothing


from copyreg import pickle
import json


class Brain:
    '''(filename) required for instance data storage\n
    creates memory for permutations of tic-tac-toe,\n
    player can ask for best_move\n
    winning games update memory'''

    # class attributes - common across all instances
    #ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8']   # no need for '9' as there is no choice to be made since only one square left

    # TODO - ERROR: I DO NEED OPTION '9' IN ALL BUT THE LAST SET OF PERMUTATIONS.  I.E. I NEED OPTION 9, BUT I DON'T NEED 9 LEVELS DEEP

    ticTacToeGrid = ['1', '2', '3']  # small list for testing only

    # constructor: see if file exists, if not create a new empty brain
    def __init__(self, playername):
        # instance attributes - particular to this instance
        filename = playername + '.dat'                                   # each instance has a separate storage file
        try: 
            # TODO consider doing a sanity check on file (e.g. sizeof) to ensure it's what we expect
            print('Brain.init: found file ', filename)
            self.f = open(filename, 'rb')
            # read in Brain dictionary from file
            self.permDictionary = json.load(self.f)
            self.f.close()
            print(f'Brain.init loaded dictionary:\n{self.permDictionary}')
        except:
            print(f'file "{filename}" not found')
            print('Brain.init: building permDictionary')
            # create a new empty brain dictionary,
            self.permDictionary = self.GetPermutations()
            print(self.permDictionary)
            # store dictionary into filename
            self.f = open(filename, 'w')
            json.dump(self.permDictionary, self.f)
            self.f.close()
            print(f'Brain.init: file {filename} created')

    def Permutate(self,stems, leaves):
        '''takes 2 strings; stems and leaves, and returns permutations by adding each leaf to each stem'''
    
        permList = []
        for stem in stems:
            availableLeaves = leaves[:] # create a copy of 'leaves' so we don't corrupt original list
            # first remove tiles that are in stem (i.e. remove tiles already used)
            for item in stem:
                availableLeaves.remove(item)

            #print(f'permutate: working on stem {stem} and leaves {availableLeaves}')
            # now we have our available tiles, add each one to each stem
            for leaf in availableLeaves:
                
                permListItem = stem + leaf
                #print(f'permutate: stem = {stem}, leaf = {leaf}, permListItem = {permListItem}  \n')
                permList.append(permListItem)

        return permList


    def GetPermutations(self):
        '''Creates a dictionary of game move permutations'''
        permutations = {}                   # this is the main dictionary that will be built up
        myStems = ['']                      # initial condition for stems

        for move in Brain.ticTacToeGrid:
            # a 'stem' is the set of move permutations so far.  e.g. [2,5] represents top middle, then centre tiles

            #while len(myStems) <= len(Brain.ticTacToeGrid):
            myStems = self.Permutate(myStems, Brain.ticTacToeGrid)
            permutations[move] = dict.fromkeys(myStems, 0)

        return permutations


    # TODO destructor: make sure files are closed before exiting
    # TODO get best_move from brain
    # TODO learn from game_result - THIS EXISTS AS LearnMoves in main prog

p1 = Brain('player1')
print('done')