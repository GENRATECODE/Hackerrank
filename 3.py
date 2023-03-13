for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    count=-1
    for j in range(1,i+1):
        print(j,end="")
        count+=1
    for k in range(i-1):
        print(count,end="")
        count-=1
    print()