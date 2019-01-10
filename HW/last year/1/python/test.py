s = input()
x = [int(i) for i in s.split()]
for i in range(len(x)):
    mini=x[i]
    index=i
    for j in range(i+1,len(x)):
        if (x[j]<mini):
            mini=x[j]
            index=j
    x[i],x[index]=x[index],x[i]
q=[]
for i in range(len(x) - 1):
    b=x[i]-x[i+1]
    q.append(b)
n=0
for j in range(len(q)-1):
    if (q[j]==q[j+1]):
        n=n+1
if (n==len(q)-1):
    print("possible")
else:
    print("impossible")