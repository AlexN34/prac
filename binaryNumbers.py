n = int(input().strip())

binary = bin(n)
# print (binary)
count = 0
maxC = 0

for i in binary:
    # print (i)
    cur = str(i)
    if cur == str(1):
        count += 1
        if count > maxC:
            maxC = count
    else:
        count = 0

print (maxC)
