s1,s2=input().split()
s3=''
s4=''
s3+=s1[0].upper()
s4+=s2[0].upper()
for i in range(len(s1)-1):
    s3+=s1[i+1].lower()
    s4+=s2[i+1].lower()
print(s3+' '+s4)
