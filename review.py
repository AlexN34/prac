import sys
# line = sys.stdin.readline() # read in one line

n = int(sys.stdin.readline()) # number of strings to parse
strings = []

for line in sys.stdin: #read as long as there's input from stdin
    if not line:
        sys.stderr.write("%s: could not read any characters" % (sys.argv[0]))
    line = line.rstrip('\n') #remove newlines
    strings.append(line)

for curString in strings:
    evenString = ""
    oddString = ""
    i = 0
    # for c in curString:
    #     if i % 2 == 0:
    #         evenString += c
    #     else:
    #         oddString += c
    #     i += 1
    # print ('About to print result:')
    for i, c in enumerate(curString):
        if i % 2 == 0:
            evenString += c
        else:
            oddString += c
    print ("%s %s" % (evenString, oddString))
