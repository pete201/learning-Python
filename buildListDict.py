GRID = ['1', '2', '3', '4']


#this works great for the inner dict
# for key in GRID:
#     myDict={}
#     shortList = GRID[:]
#     #shortList.remove(key)
#     myDict[key] = dict.fromkeys(shortList,0)
#     print('initial: ',myDict)



def CreateDict(alist):
    '''from (list), extracts each vlaue and builds dictionary of remaining values'''
    innerDict = {}
    for key in alist: 
        shortList = alist[:]
        shortList.remove(key)
        innerDict[key] = dict.fromkeys(shortList,0)      
    return (innerDict)

def main():
    ''''''
    # first establish List with initial values from Grid (i.e. the suggestion values for first move)
    ListDics = [dict.fromkeys(GRID,0)]
    mylist = GRID[:]        # copy list 
    
    myDict = CreateDict(mylist)
    #print(myDict)
    ListDics.append(myDict)
    print(ListDics)
    

if __name__ == '__main__':
    main()