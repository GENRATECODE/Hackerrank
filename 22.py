'''You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the  sets N.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set[1,3,4] is a strict superset of set([1,3]).
Set ([1,3,4])is not a strict superset of set([1,3,4]).
Set ([1,3,4])is not a strict superset of set([1,3,5]).

Input Format

The first line contains the space separated elements of set A.
The second line contains integer N , the number of other sets.
The next  N lines contains the space separated elements of the other sets.

Constraints

Output Format

Print True if set  is a strict superset of all other  sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output 0

False
Explanation 0

Set  is the strict superset of the set but not of the set because  is not in set .'''
set1=set(map(int,input().split()))
result=[]
for i in range(int(input())):
    flag=False
    set2=set(map(int,input().split()))
    if set1.issuperset(set2):
        result.append(True)
    else:
        result.append(False)
if False in result:
    print(False)
else:
    print(True)