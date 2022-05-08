n = int(input('number of lectures='))
testlist=list(map(int, input().split()))
max = max(testlist)

newlist = []

for score in testlist:
    newlist.append(score/max*100)

testavg = sum(newlist)/n
print(testavg)