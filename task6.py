from math import *

print("Enter the number: ")
x = int(input())
composite = False
for d in range(2, ceil(sqrt(x)) + 1):
    if x % d == 0:
        composite = True
        break

if composite and x != 2:
    print("Composite")
else:
    print("Prime")
