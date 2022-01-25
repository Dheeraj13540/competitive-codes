'''
Varun is the founder of Event Management Company, "Sparsh Service".
In the company all the financial transaction are carried out online and varun has strictly
insisted his staff to do any transactions on web browsers that supports AES encryption
nubbers. A number is an AES number if it has exactly four divisors. in other words,
there are exactly four numbers that devide into it evenly. For example, 10 is an ASE
number because it has exactly four devisors (1,2,5,10). 12 is not an AES number because
it has too many devisors (1,2,3,4,6,12). 11 is not an AES number either. write a program
that counts how many numbers from that range are AES numbers.

input range: 1,20
output : 5
input range: 50,1000
output : 277
'''
a=int(input())
b=int(input())
co=0
for i in range(a,b):
    c = []
    for j in range(1,i+1):
        if i%j==0:
            c.append(j)
    if len(c)==4:
        co= co+1
print(co)
