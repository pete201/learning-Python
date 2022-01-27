# class to set up memory locations for every permutation of tic tac toe
# memory locations will be populated vlaues indicating likelihood of winning move
# if a move is a winning move, +1, if it's a losing move -1, for a draw do nothing


class Brain:
    '''(filename) required for instance data storage\n
    creates memory for permutations of tic-tac-toe,\n
    player can ask for best_move\n
    winning games update memory'''

    # class attributes - common across all instances
    #ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8']   # no need for '9' as there is no choice to be made since only one square left
    ticTacToeGrid = ['1', '2', '3']  # small list for testing only

    # constructor: see if file exists, if not create a new empty brain
    def __init__(self, filename):
        # instance attributes - particular to this instance

        # TODO move this away from assignments into its own function area
        self.f = filename + '.dat'                                   # each instance has a separate storage file
        #print('brain:constructor', f)
        try: 
            # TODO consider doing a sanity check on file (e.g. sizeof) to ensure it's what we expect
            self.f = open('myfile.dat', 'rb')
        except:
            print(f'file "{self.f}" not found')
            print('Brain.init: building permDictionary')
            # create a new empty brain dictionary,
            self.permDictionary = self.GetPermutations()
            print(self.permDictionary)
            # TODO pickle and file with filename.dat

    def Permutate(self,stems, leaves):
        '''takes 2 strings; stem and leaves, and returns permutations by adding each leaf to each stem'''
    
        permList = []

        for stem in stems:
            #first find leaves that are not in stem
            availableLeaves = leaves[:] # this creates a copy so we don't corrupt original list

            for item in stem:
                availableLeaves.remove(item)
            
            #print(f'permutate: working on stem {stem} and leaves {availableLeaves}')
            # now we have our availableLeaves, add each one to each stem
            for leaf in availableLeaves:
                
                permListItem = stem + leaf
                #print(f'permutate: stem = {stem}, leaf = {leaf}, permListItem = {permListItem}  \n')
                permList.append(permListItem)

        return permList


    def GetPermutations(self):
        permutations = {}                   # this is the main dictionary that will be built up
        
        myStems = ['']          # initial condition for stems

        for move in Brain.ticTacToeGrid:
            myStems = self.Permutate(myStems, Brain.ticTacToeGrid)
            permutations[move] = dict.fromkeys(myStems, 0)

        return permutations

    # TODO add permutate as private function that __init__ can call
    # TODO destructor: make sure files are closed before exiting
    # TODO get best_move from brain
    # TODO learn from game_result - THIS EXISTS AS LearnMoves in main prog

p1 = Brain('player1')
print('done')