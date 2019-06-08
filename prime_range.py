import math
l,u=input().split()
prime=[]
for i in range(int(l),int(u)+1):
    prime.append(i)
i=2
while(i <= int(math.sqrt(int(u)))):
    if i in prime:
        for j in range(i*2, int(u)+1, i):
            if j in prime:
                prime.remove(j)
    i = i+1
print(*prime)
