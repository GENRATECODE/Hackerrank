"""
    Sample Input

ABCDCDC
CDC
Sample Output
2
"""
def count_substring(string, sub_string):
    string_count = len(string)
    sub_string_count = len(sub_string)
    c=0
    for i in range(string_count):
        if sub_string==string[i: (sub_string_count+i)]:
            c=c+1
    return c
string="ABCDCDC"
sub_string="CDC"
print(count_substring(string,sub_string))