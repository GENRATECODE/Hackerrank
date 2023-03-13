def operation(time_len,s):
    for i in range(time_len):
        command=list(input().split())
        if len(command)==1 and command[0]=="pop":
            s.pop()
            print(s)
        elif len(command)==2 and command[0]=="remove":
            s.remove(int(command[1]))
            print(s)
        elif len(command)==2 and command[0]=="discard":
            s.discard(int(command[1]))
            print(s)
    print(*s)
if __name__=='__main__':
    n = int(input())
    s = set(map(int, input().split()))
    time_len=int(input())
    operation(time_len,s)