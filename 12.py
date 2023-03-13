# reverse binary operation
def rev(a):
    b=""
    for i in a:
        b=i+b
    return b
#main problem start
def octal(number):
    a=""
    while number!=0:
        if number%8==1 or number%8==2 or number%8==3 or number%8==4 or number%8==5 or number%8==6 or number %8==7:
            a+=str(number%8)
        elif number%8==0:
            a+="0"
        number//=8
    return rev(a)

def hexadecimal(number):
    a=""
    while number!=0:
        if number%16==1 or number%16==2 or number%16==3 or number%16==4 or number%16==5 or number%16==6 or number %16==7 or number%16==8 or number%16==9:
            a+=str(number%16)
        elif number%16==10:
            a+="A"
        elif number%16==11:
            a+="B"
        elif number%16==12:
            a+="C"
        elif number%16==13:
            a+="D"
        elif number%16==14:
            a+="E"  
        elif number%16==15:
            a+="A"
        elif number%16==0:
            a+="0"
        number//=16
    return rev(a)
#binary 
def binary(n):
    a=""
    while n!=0:
        if n%2==0 :
            a+=str(0)
        if n%2==1:
            a+=str(1)
        n=n//2
    return rev(a)
def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print((str(i)).rjust(1),(octal(i)).rjust(1),(hexadecimal(i)).rjust(1),(binary(i)).rjust(1))
if __name__ == '__main__':
    number=int(input())
    print_formatted(number)
#there are two way to make this program.