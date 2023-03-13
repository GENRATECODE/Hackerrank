def merge(_set:set)->str:
    _list=list(_set)
    sum=""
    for i in _list:
        sum+=i
    return sum
def merge_the_tool(string:str,k:int)->str:
    string_list=list(string)
    str_len=int(len(string)/k)
    count=0
    ans=list()
    flag=0
    for i in range(str_len):
        result=list()
        for j in range(k):
            if string_list[count]  not in  result:
                result.append(string_list[count])
            count+=1
        ans.append(merge(result))
    return ans
string=input()
k=int(input())
result=merge_the_tool(string,k)
print(*result)