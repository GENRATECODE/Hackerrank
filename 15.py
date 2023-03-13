
'''
\hr-challenge-images\9693\1450330231-04db904008-banana.png

'''

def minion_game(string):
    # your code goes here
    kevin,stuart=0,0
    for i in range(len(string)):
        if string[i] in "AIEOU":
            kevin+=(len(string)-i)
        else:
            stuart+=(len(string)-i)
    if kevin>stuart:
        print("Kevin",kevin)
    elif kevin ==stuart:
        print("Draw")
    else:
        print("Stuart",stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)