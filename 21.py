'''
You are given two sets, A and B.
Your job is to find whether set  A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A .
The second line of each test case contains the space separated elements of set A .
The third line of each test case contains the number of elements in set B .
The fourth line of each test case contains the space separated elements of set B .

Constraints
 * 0<t<21
 * 0<Number of element in each set <1001
Output Format

Output 
True or False for each test case on separate lines.
'''
test_case=int(input())
for i in range(test_case):
    no_a_set=input()
    set1=set(map(int,input().split()))
    no_a_set=input()
    set2=set(map(int,input().split()))
    print(set1.issubset(set2))