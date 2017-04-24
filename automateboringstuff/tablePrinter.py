#!/usr/bin/python3
#assume all inner lists have same number of strings
def printTable(strList):
    colWidths = [0] * len(strList)
    index = 0
    print (colWidths)
    for str in strList:
        print (str)
        for i in str:
            if (len(i) > colWidths[index]):
                colWidths[index] = len(i)
            else:
                continue
        print (colWidths[index])
        index += 1
    rightWidth = max(colWidths)

    """
    Ugly solution.. uses first list of strings to prepredict how long each one will be
    Need to find out how to access length of inside list BEFORE accessing outside list
    """
    listLength = len(strList[0]) 
    tableStr = ""
    for i in range(listLength):
        for j in range(len(strList)): #all inner lists have same length
            tableStr += strList[j][i].rjust(rightWidth)
        tableStr = tableStr.rstrip()
        tableStr += "\n"
    print (tableStr)
    print (rightWidth)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
