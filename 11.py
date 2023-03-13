'''
Sample Input
9 27
Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''

row,colum=map(int,input().split())
hypen="-"
dot=".|."
odd=1
word="WELCOME"
left_right=(colum-3)//2
remain_distance=(colum-len(word))//2
loop=row//2
print(remain_distance)
for i in range(loop):
    print((hypen*left_right).ljust(0)+(dot*odd).center(0)+(hypen*left_right).rjust(0))
    odd+=2
    left_right-=3

print((hypen*remain_distance).ljust(0)+(word).center(0)+(hypen*remain_distance).rjust(0))
left_right=3
for j in range(loop):
    odd-=2
    print((hypen*left_right).ljust(0)+(dot*odd).center(0)+(hypen*left_right).rjust(0))
    left_right+=3
