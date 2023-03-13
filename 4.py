def google(s:str)->dict:
    result=dict()
    count=1
    for i in s:
        
        result[i]=count
    print(result)
s=input()
google(s)