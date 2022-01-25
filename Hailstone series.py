'''
Hailstone series:-

if the number x is even then next number will be x/2
otherwise print 3x+1 .

input : starting no: 17, no of terms to generate: 5
output:- 17,52,26,13,40
input : starting no: 6, no of terms to generate: 9
output: 6,3,10,5,16,8,4,2,1
'''


a=int(input())
b=int(input())
c=a
print(a)
for i in range(b-1):
    if c%2==0:
        print(c//2)
        c=c//2
    else:
        c=3*c+1
        print(c)
