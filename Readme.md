ListDictionary branch notes

with previous dictionary, i could not access the list of recommended values very well

here i have opted for a deeper nested dictionary approach.

each move contains a dictionary, and the moves are wrapped in a list
i use a list to distinguish 'game move' from a tile number
so the first ref is a game move integer, followed by tile ref strings...

    [0] - no moves have been made - show all possibilities
    [0][2] - no mvoes, show value of tile 2
    [2][2][3] - 2 moves made, first was '2', second was '3' - show all possibilities.