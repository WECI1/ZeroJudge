t=int(input())

for i in range(t):
    a,b,c,d=map(int,input().split())
    if b-a==d-c:
        print(a,b,c,d,d+(d-c))

    else:
        print(a,b,c,d,d*(d//c))