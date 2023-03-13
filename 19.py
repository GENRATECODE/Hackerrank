"""Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output

38
explanation
After the first operation, (intersection_update operation), we get:
set A=set([1,2,3,4,5,6,7,8,9,11])

After the second operation, (update operation), we get:
set A=SET([1,2,3,4,5,6,7,8,,9,11,55,66])

After the third operation, (symmetric_difference_update operation), we get:
set A=SET([1,2,3,4,5,6,7,8,,9,11,22,35,55,58,62,66])

After the fourth operation, ( difference_update operation), we get:
set A=SET([1,2,3,4,5,6,7,8,9])

The sum of elements in set  A after these operations is 38."""
def operation(time_len,s):
    for i in range(time_len):
        command=list(input().split())
        if "intersection_update" in command:
            s.intersection_update(set(map(int,input().split())))
            print(s)
        elif "update" in command:
            s.update(set(map(int,input().split())))
            print(s)
        elif "symmetric_difference_update" in command:
            s.symmetric_difference_update(set(map(int,input().split())))
            print(s)
        elif "difference_update" in command:
            s.difference_update(set(map(int,input().split())))
            print(s)
    sum=0
    for i in s:
        sum+=i
    print(sum)
if __name__=='__main__':
    n = int(input())
    s = set(map(int, input().split()))
    time_len=int(input())
    operation(time_len,s)