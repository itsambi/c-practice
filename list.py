if __name__ == '__main__':
    N = int(input())
    xy = []
    for i in range(0, N):
        cmd = input().split()
        if cmd[0] == "insert":
            xy.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "append":
            xy.append(int(cmd[1]))
        elif cmd[0] == "pop":
            xy.pop()
        elif cmd[0] == "print":
            print(xy)
        elif cmd[0] == "remove":
            xy.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            xy.sort()
        else:
            xy.reverse()