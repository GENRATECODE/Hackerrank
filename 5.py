from itertools import product

K, M = map(int,input().split())

N = (list(map(int, input().split()))[1:] for _ in range(K))
max_lst = []
for i in product(*N):
    print(i)
for item in product(*N):
    S = 0
    for val in item:
        print("ceck",val)
        S += val**2
    print(S)
    S_max = S % M
    max_lst.append(S_max)
print(max(max_lst))
