GRID = ['1', '2', '3', '4']


def BuildNestedDict(input_dict):
    returnDict = {}
    #print('BuildNestedDict: input_dict:', input_dict)  
    for input_key, input_value in input_dict.items():
        #print('BuildNestedDict: type(element)', type(input_value))
        if type(input_value) is dict:   # if it's a nested dictionary, then recursive call.  If not, then we work on input dictionary
            #print('BuildNestedDict: recursivne call----------------------------------------')
            returnValue = BuildNestedDict(input_value)
            #print('BuildNestedDict: itteration return value:', returnValue)
            #print('BuildNestedDict: and mykey:', input_key)
            #innerDict['1'].update(BuildNestedDict(value))
            returnDict[input_key] = returnValue
            #print('BuildNestedDict: returnDict so far...', returnDict)
        else:
            # we get here if type NOT dictionary
            valsList = list(input_dict.keys())   # create a list of the keys in innermost dictionary so far
            #print('BuildNestedDict: valsList:', valsList)
            for key in valsList: 
                shortList = valsList[:]
                shortList.remove(key)
                returnDict[key] = dict.fromkeys(shortList,0) 

    print('BuildNestedDict: returnDict:', returnDict)
    return returnDict


def main():
    ''''''
  
    # # first establish List with initial dictionary from Grid (i.e. the suggestion values for first move)
    ListDics = [dict.fromkeys(GRID,0)]

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