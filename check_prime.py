import math
import time

def prime(n):
    for i in range (2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
            break
    return True

st = time.time()
print(prime(10**100 + 3))
et = time.time()
print(f"time = {et-st}")
    
    

            

    