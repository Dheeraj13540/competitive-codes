'''Write a program that takes a string, and returns a new string with any duplicate consecutive letters removed.

Example

"ppoeemm" -> "poem"

"wiiiinnnnd" -> "wind"
'''

a=input()
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end="")
