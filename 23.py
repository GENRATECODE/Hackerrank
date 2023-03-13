hap=0
n,m=map(int,input().split())
set1=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
for i in set1:
    if i in a:
        hap+=1
    elif i in b:
        hap-=1
print(hap)
'''
Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.
Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain 1 unit of happiness for elements 3  and  1 in set 1. You lose 1 unit for  5 in set B. The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1=1.
'''