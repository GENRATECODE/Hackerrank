def solve(s):
    s=list(s.split())
    temp=[]
    for i in s:
        print(i)
        temp.append(i.capitalize())
    return " ".join(temp)
def solve1(s):
    cp=""
    for i in range(len(s)):
        if i==0:
            cp+=s[i].capitalize()
        elif s[i-1]==" " and s[i]!=" ":
            cp+=s[i].capitalize()
        else:
            cp+=s[i]
    return cp
j=input()
print(solve(j))
print(solve1(j))
"""Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
"""