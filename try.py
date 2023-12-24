s="titt"
t="titt"


d1={}
d2={}
for i in s:
    d1[i]=d1.get(i,0)+1
for j in t:
    d2[j]=d2.get(j,0)+1



print(d1,d2)
for c in d1:
    if d1[c] == d2[c]:
        print("ana")