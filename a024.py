num1,num2=map(int,input().split())

a=max(num1,num2)
b=min(num1,num2)
c=a%b

while c!=0:
    a=b
    b=c
    c=a%b
print(b)