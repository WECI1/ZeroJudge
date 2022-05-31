import sys

for i in sys.stdin:
    a=int(i)
    if a%4==0 and a%100!=0:
        print("閏年")
    elif a%400==0:
        print("閏年")
    else:    
        print("平年")
        