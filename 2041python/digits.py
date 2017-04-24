import sys

trantab = str.maketrans("0123456789", "<<<<<5>>>>")

for line in sys.stdin.readlines():
    print (line.translate(trantab))
