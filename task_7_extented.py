import math
import time
start=time.time()
pnth = 10001
x = 1
prime = [2]
while (len(prime) < pnth):
    x  += 2
    print(x)
    for i in prime:
        if x%i == 0:
            break
        if (i > math.sqrt(x)):
            prime.append(x)
            break

print(prime[0])
end=time.time()
print(end-start)