def printToN(n):
    result = ""
    if n > 1 :
        for i in range(1, n):
            result += str(i)
        print(result + str(n))
    else:
        print(1)
if __name__ == "__main__":
    n = int(input())
    printToN(n)
