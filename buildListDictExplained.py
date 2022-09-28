


def BuildNestedDict(input_dict):
    returnDict = {}
    #print('BuildNestedDict: input_dict:', input_dict)  
    for input_key, input_value in input_dict.items():
        #print('BuildNestedDict: type(element)', type(input_value))
        if type(input_value) is dict:   # if it's a nested dictionary, then recursive call.  If not, then we work on input dictionary
            #print('BuildNestedDict: recursivne call----------------------------------------')
            returnDict[input_key] = BuildNestedDict(input_value)
            #print('BuildNestedDict: and mykey:', input_key)
            #print('BuildNestedDict: returnDict so far...', returnDict)
        else:
            # we get here if type NOT dictionary
            valsList = list(input_dict.keys())   # create a list of the keys in innermost dictionary so far
            #print('BuildNestedDict: valsList:', valsList)
            for key in valsList: 
                shortList = valsList[:]
                shortList.remove(key)
                returnDict[key] = dict.fromkeys(shortList,0) 

    #print('BuildNestedDict: returnDict:', returnDict)
    return returnDict


def main():
    ''''''
    GRID = ['1', '2', '3', '4']
    # first establish List with initial dictionary from Grid (i.e. the suggestion values for first move)
    ListDics = [dict.fromkeys(GRID,0)]

    #now pass this dictionary to BuildNestedDictionary n times where n = len(GRID)-1
    for n in range (len(GRID)-1):
        ListDics.append(BuildNestedDict(ListDics[-1]))
    
    #print('main: ListDics[1]:',ListDics)

    print()
    #now I can set or get any desired move
    #print(ListDics[0])
    print(ListDics[1]['1'])
    print(ListDics[1]['2'])
    ListDics[1]['1']['2'] = 1
    print(ListDics[1]['1'])

    

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

this results in correct list of nested dictionaries:
[
{'1': 0, '2': 0, '3': 0, '4': 0}, 
{
'1': {'2': 0, '3': 0, '4': 0}, '2': {'1': 0, '3': 0, '4': 0}, '3': {'1': 0, '2': 0, '4': 0}, '4': {'1': 0, '2': 0, '3': 0}
}, 
{
'1': {'2': {'3': 0, '4': 0}, '3': {'2': 0, '4': 0}, '4': {'2': 0, '3': 0}}, 
'2': {'1': {'3': 0, '4': 0}, '3': {'1': 0, '4': 0}, '4': {'1': 0, '3': 0}}, 
'3': {'1': {'2': 0, '4': 0}, '2': {'1': 0, '4': 0}, '4': {'1': 0, '2': 0}}, 
'4': {'1': {'2': 0, '3': 0}, '2': {'1': 0, '3': 0}, '3': {'1': 0, '2': 0}}
}, 
{
'1': {'2': {'3': {'4': 0}, '4': {'3': 0}}, '3': {'2': {'4': 0}, '4': {'2': 0}}, '4': {'2': {'3': 0}, '3': {'2': 0}}}, 
'2': {'1': {'3': {'4': 0}, '4': {'3': 0}}, '3': {'1': {'4': 0}, '4': {'1': 0}}, '4': {'1': {'3': 0}, '3': {'1': 0}}},
'3': {'1': {'2': {'4': 0}, '4': {'2': 0}}, '2': {'1': {'4': 0}, '4': {'1': 0}}, '4': {'1': {'2': 0}, '2': {'1': 0}}}, 
'4': {'1': {'2': {'3': 0}, '3': {'2': 0}}, '2': {'1': {'3': 0}, '3': {'1': 0}}, '3': {'1': {'2': 0}, '2': {'1': 0}}}
}
]
'''