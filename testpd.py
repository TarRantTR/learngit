s=[]
for i in range (10):
    x = int(input("shjushu"))
    s[i-1].append(x)
for i in range(9):
    for j in range(i+1,10):
        if s[i]>s[j]:
            s[i],s[j] = s[i],s[j]


