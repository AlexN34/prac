def tutBoard():
    tutBoard = { 'top-L' : 'top-L', 'top-M' : 'top-M', 'top-R' : 'top-R',
                'mid-L' : 'mid-L', 'mid-M' : 'mid-M', 'mid-R' : 'mid-R',
                'low-L' : 'low-L', 'low-M' : 'low-M', 'low-R' : 'low-R'}
    printBoard(tutBoard)
    
theBoard = { 'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
             'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
             'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}
def printBoard (board):
    print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('- + - + - ')
    print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('- + - + - ')
    print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])

curPlayer = 1
while True:
    tutBoard()
    #prevent from marking taken tile
    move = str(input('Please indicate which tile you want to mark (see above)').strip())
    if curPlayer == 1:
        marker = 'X'
    else:
        marker = 'O'
    theBoard[move] = marker
    print ('Latest board :')
    printBoard(theBoard)
    curPlayer *= -1

    #win condition
