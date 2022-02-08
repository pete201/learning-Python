GRID = ['1', '2', '3', '4']


#this works great for the inner dict
# for key in GRID:
#     myDict={}
#     shortList = GRID[:]
#     #shortList.remove(key)
#     myDict[key] = dict.fromkeys(shortList,0)
#     print('initial: ',myDict)



def CreateDict(keysList, valsList):
    '''from (list), extracts each vlaue and builds dictionary of remaining values'''
    outerDict = {}
    for k in keysList:
        innerDict = {}
        for key in valsList: 
            shortList = valsList[:]
            shortList.remove(key)
            innerDict[key] = dict.fromkeys(shortList,0)  
        outerDict[k] = innerDict # add innerDict to outerDict    
    return (outerDict)

def BuildNestedDict(input_dict):
    #outerDict = {}
    print('BuildNestedDict: input_dict:', input_dict)
    innerDict = {}
    for element in input_dict.values() :
        print('BuildNestedDict: type(element)', type(element))
        
        if type(element) is dict:   # if it's a nested dictionary, then recursive call.  If not, then we work on input dictionary
            print('BuildNestedDict: recursivne call----------------------------------------')
            innerDict.update(BuildNestedDict(element))
        # we get here is type NOT dictionary
        valsList = list(input_dict.keys())   # create a list of the keys in innermost dictionary so far
        print('BuildNestedDict: valsList:', valsList)
        for key in valsList: 
            shortList = valsList[:]
            shortList.remove(key)
            innerDict[key] = dict.fromkeys(shortList,0) 
        print('BuildNestedDict: return inner:', innerDict)
        return innerDict


def main():
    ''''''
    # # first establish List with initial values from Grid (i.e. the suggestion values for first move)
    # ListDics = [dict.fromkeys(GRID,0)]
    # myValslist = GRID[:]        # copy list 
    # #mylist = list(ListDics[-1].keys())
    # print(myValslist)
    # myKeysList = [0]

    # myDict = CreateDict(myKeysList, myValslist)
    # print('myDict:', myDict)
    # ListDics.append(myDict)
    # print('ListDics:', ListDics)
    # print('ListDics[0]:', ListDics[-1])
    # print('ListDics[0].keys:', list(ListDics[-1].keys()))
    # print('ListDics[-].values:', list(ListDics[-1].values()))

    # # the 'list' i pass should be the list of keys from previous dictionary
    # # so for first pass, this is simply 1,2,3,4 from keys from dictionary [0]
    # # TODO lets start printing out the lists of keys...

    # # first establish List with initial dictionary from Grid (i.e. the suggestion values for first move)
    ListDics = [dict.fromkeys(GRID,0)]
    #print('main: ListDics:',ListDics)
    #now pass this dictionary to BuildNestedDictionary
    ListDics.append(BuildNestedDict(ListDics[0]))
    print('main: ListDics[0]:',ListDics)
    ListDics.append(BuildNestedDict(ListDics[1]))
    print('main: ListDics[1]:',ListDics)

    

if __name__ == '__main__':
    main()

# TODO to recursively act on nested dictionary, i need a function that calls itself
'''
psuedocode

def fn(nested_dict):
        for element in nested_dict:
            if element TYPE == dict:
                fn(element)
            # we get here is type NOT dictionary
            remove each element in turn
            dict from keys
'''