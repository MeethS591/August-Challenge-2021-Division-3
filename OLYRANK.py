n = int(input())
for i in range(n):
    meds = list(map(int,input().split()))
    win1 = meds[0]+meds[1]+meds[2]
    win2 = meds[3]+meds[4]+meds[5]
    if win1>win2:
        print(1)
    else:
        print(2)