'''You are given a string  Sand width W.
Your task is to wrap the string into a paragraph of width W.
Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ'''
import textwrap
def wrap(string, max_width):
    wrapper=textwrap.TextWrapper(width=max_width)
    word_list=wrapper.wrap(text=string)
    result=""
    for i in word_list:
        result+=i+'\n'
    return result 

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)