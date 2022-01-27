# build a nested dictionary
# 'Permutate' function takes 2 lists: stems and leaves, and add each leaf to each stem



def Permutate(stems, leaves):
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


def GetPermutations():
    permutations = {}                   # this is the main dictionary that will be built up
    #ticTacToeGrid = ['1', '2', '3', '4', '5', '6', '7', '8']   # no need for '9' as there is no choice to be made since only one square left
    ticTacToeGrid = ['1', '2', '3']  # small list for testing only
    myStems = ['']          # initial condition for stems

    for move in ticTacToeGrid:
        myStems = Permutate(myStems, ticTacToeGrid)
        permutations[move] = dict.fromkeys(myStems, 0)

    return permutations


def main():
    
    myPermDictionary = GetPermutations()

    print('perms = ',myPermDictionary)

    print()
    print('length of dictionary is:',sum(len(v) for v in myPermDictionary.values()))


if __name__ == "__main__":
    main()



