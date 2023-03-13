'''
Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12'''
def sym_dif(set1:set,set2:set)->list:
    return set1.symmetric_difference(set2)

if __name__=="__main__":
    n=4
    set1={8,-10}
    set2={5,6,7}
    m=4
    res=sym_dif(set1,set2)
    print(sorted(res),max(res))
    for i in sorted(res):
        print(i)