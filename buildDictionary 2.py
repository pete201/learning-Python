# build a nested dictionary
# 'Permutate' function takes 2 lists: stems and leaves, and add each leaf to each stem


permutations = {}                   # this is the main dictionary that will be built up
#refNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']   # no need for '9' as there is no choice to be made since only one square left
refNumbers = ['1', '2', '3', '4'] 


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



myStems = ['']          # initial condition for stems

for move in refNumbers:
    myStems = Permutate(myStems, refNumbers)
    permutations[move] = dict.fromkeys(myStems, 0)

print('perms = ',permutations)

print()
print('length of dictionary is ',sum(len(v) for v in permutations.values()))

exit()



