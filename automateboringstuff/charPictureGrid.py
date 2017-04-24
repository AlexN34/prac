grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', ],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.', 'z'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', 'b', 'c'],
        ['a']]

# print (grid)
# print ("i: %s, j: %s" % (i, j))
# print (grid[i][j], end="")
lengths = [len(grid)]
for row in grid:
    lengths.append(len(row))

print (lengths)
dim = max(lengths)

print (dim)
for j in range(dim): #length of this is number of columns - grid[i].. but not defined
    #just skip if can't print them - ideally, know sizes of each ahead of time.
    try:
        for i in range(dim): #length of this is number of rows
            # print (grid[i], end="BLAH")
            print (grid[i][j], end="")
    except IndexError:
        print("*", end="")
    print("")
