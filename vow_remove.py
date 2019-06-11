w=int(input())
s=input()
l=list(s)
lis=['a','e','i','o','u','A','E','I','O','U']
for i in (l):
    if i in lis:
        l.remove(i)
new_l=l[::-1]
s="".join(new_l)
print(s)
