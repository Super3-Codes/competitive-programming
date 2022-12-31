n,m = map(int,input().split())
an_aray = list(map(int,input().split()))
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))
adict={}
score = 0
for x in an_aray:
    if x not in adict.keys():
        adict[x] = 0
    adict[x]+=1
for x,y in adict.items():
    if x in setA:
        score += y
    if x in setB:
        score -= y
print(score)
