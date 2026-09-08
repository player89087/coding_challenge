
import random
import numpy as np
from sympy import factorint

# Miller-Rabin primality test 
def miller_rabin(n, iterations):
    if n in {2, 3}:
        return n, True, f'{(1-4**-iterations)*100} %'
    for iteration in range(iterations):
        k = random.randint(2, n-2)
        
        a = (n-1)
        seq = []
        while True:
            seq.append(pow(k,a, n))
            if a % 2 == 0 and a != 0:
                a //= 2
            else:
                break
        if validad_seq(seq, n) == False:
            return n, False, '100 %'
    return n, True, f'{(1-4**-iterations)*100} %'

def validad_seq(seq, n):
    for num in seq:
        if num == 1:
            continue
        elif num == n-1 and len(seq)>1:
            return True
        else:
            return False
    return True


n = 10 #bit-size, if bigger loss in efficiency compared to gain in secruity 
is_prime = False
test_num = 2**n
while is_prime == False:
    test_num += 1
    prime, is_prime, percentage = miller_rabin(test_num, 10)
    #print(f'1e+{n} {test_num-2**n}/{n*int(np.log(float(2)))} {is_prime} {percentage}')



# Diffie-Hellman-key-exchange 

p = test_num 
print(p)

factors = factorint(p-1)

for g in range(2, 100):
    if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
        break
print(g)