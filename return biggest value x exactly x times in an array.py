A=[3,8,2,3,3,2]
A.sort()
f=0
for i in range(len(A)):
    if A.count(A[i])==A[i]:
        f=A[i]
print(f)
