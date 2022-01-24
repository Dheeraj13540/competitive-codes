1. Given A=[3, 8, 2, 3, 3, 2] the function should return 3. The value 2 occurs exactly two times and the value 3 occurs exactly three times,
   so they both meet the task conditions. The value 8 occurs just once, thus it does not meet the task conditions. The maximum of 2 and 3 is 3

2. Given A-[7, 1, 2, 8, 2] the function should return 2. The value 1 occurs exactly one time, the value 2 occurs exactly two times.

3. Given A=[3, 1, 4, 1, 5] the function should return 0. There is no value

which meets the task conditions,

Test Output

4. Given A [5, 5, 5, 5, 5] the function should return 5.

            
A=[3,8,2,3,3,2]
A.sort()
f=0
for i in range(len(A)):
    if A.count(A[i])==A[i]:
        f=A[i]
print(f)
