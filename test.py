n=int(input("size"))
data=[]
scaned=[]
for i in range(n):
    data.append(input("data"))
for words in data:
    if words not in scaned:
        a=data.count(words)
        scaned.append(words)
        print(a,end=" ")