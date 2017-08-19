#!/usr/bin/python
def ListOps(N):
    i = 0
    result = []
    while i < N:
        cmd_list = str(input()).split(" ")
        if cmd_list[0] == "insert":
            result.insert(int(cmd_list[1]), int(cmd_list[2]))
        elif cmd_list[0] == "print":
            print(result)
        elif cmd_list[0] == "remove":
            result.remove(int(cmd_list[1]))
        elif cmd_list[0] == "append":
            result.append(int(cmd_list[1]))
        elif cmd_list[0] == "sort":
            result.sort()
        elif cmd_list[0] == "pop":
            result.pop()
        elif cmd_list[0] == "reverse":
            result.sort(reverse=True)
        i += 1


if __name__ == '__main__':
    N = int(input())
    ListOps(N)
