t = int(input())
for i in range(t):
    a = list(map(int,input().split()))
    s = set(a)
    if len(s)==4:
        print(2)
    elif len(s)==3:
        print(2)
    elif len(s)==2:
        if a.count(a[0])==2:
            print(2)
        else:
            print(1)
    else:
        print(0)