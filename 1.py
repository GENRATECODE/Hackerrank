"""Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are  students in this class whose names and grades are assembled 
to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], 
['Akriti', 41], ['Harsh', 39]]"""
vote=[]
score_set=set()
result=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    vote.append([name,score])
    score_set.add(score)
score_set=sorted(set(score_set))
score_list=list(score_set)
score_list.remove(min(score_list))
check=score_list[0]
for i in vote:
    if i[1]==check:
        result.append(i[0])
result.sort()
for i in result:
    print(i)
