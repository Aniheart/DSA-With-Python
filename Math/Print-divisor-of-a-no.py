from typing import List
import math

def printDivisors(n) -> List[int]:
    li = []
    x =int(math.sqrt(n))+1
    for i in range(1,x):
        if(n%i==0):
            li.append(i)
            if(i != n//i):
                li.append(n//i)
    li.sort()
    return li
n = int(input("Enter: "))
sol = printDivisors(n)
print(*sol)


