a=input().split()
M=int(a[0])
D=int(a[1])
S=(M*2+D)%3

if S==0:
    print("普通")
if S==1:
    print("吉")
if S==2:
    print("大吉")