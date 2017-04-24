import sys

n = int(input())

phoneNumbers = {}
for i in range(0, n):
    line = sys.stdin.readline().strip();
    terms = line.split(' ')
    # print ('read in terms: i = %d, line - %s, terms 0 - %s 1 - %s' % (i, line, terms[0], terms[1]))
    phoneNumbers.update({terms[0]: terms[1]})

# print ('Input completed. Contents are:')
# for val in phoneNumbers:
#     print (val)
#     print (phoneNumbers.get(val))

for inputLine in sys.stdin:
    line = inputLine.strip()
    # print ('about to print terms: line - %s' % (line))
    try:
        print("%s=%s" % (line, phoneNumbers[line]))
    except KeyError:
        print ('Not found')
