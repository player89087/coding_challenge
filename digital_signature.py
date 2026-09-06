import hashlib
import random 
import math 
import time 
import numpy as np 

file_path = "/home/siredgar20/Schreibtisch/coding_challenge/challenge/level0/start.html"
hash_func = hashlib.new("sha-256")
    
with open(file_path, 'rb') as file:
    # 8192 bits since its most efficient that way 
    while chunk := file.read(8192):
        hash_func.update(chunk)
    



hash_bytes = hash_func.digest()      # to gain real bytes
hash_int = int.from_bytes(hash_bytes, "big") # first  bit is highest byte




# calculate rsa key pair 


prime_numb = []

nums = []




def miller_rabin(candidate, iterations):
    if candidate in {2, 3}:
        return candidate, True, f'{(1 - 4**-iterations)*100} %'
    
    for iteration in range(iterations):
        k = random.randint(2, candidate - 2)
        a = candidate - 1
        seq = []
        while True:
            seq.append(pow(k, a, candidate))
            if a % 2 == 0 and a != 0:
                a //= 2
            else:
                break
        if not validad_seq(seq, candidate):
            return None, False, '100 %'  # no prime found 
    
   
    return candidate, True, f'{(1 - 4**-iterations)*100} %'

def validad_seq(seq, candidate):
   
    for num in seq:
        if num == 1:
            continue
        elif num == candidate - 1 and len(seq) > 1:
            return True
        else:
            return False
    return True


p_q = []
nums = 0

for i in range(2): # amount specified 
    is_prime = False
    k = random.randint(0, 10000000) 
    power = random.randint(3072,4096) # higher to make it more secure, may include padding in the future

    test_num = 2**power + k
    while is_prime == False:
        nums += 1
        if test_num+nums % 2 != 0:
            prime, is_prime, percentage = miller_rabin(test_num+nums, 1000) # precision over 5,10 
        if nums % 100 == 0:
            print(f'checked numbers {nums} \t  nums found {i}')
    p_q.append(test_num +  nums)



p = p_q[0]
q = p_q[1]



n = p * q 
 # thats important 
# φ(p⋅q)=(p−1)*(q−1)
phi = (p-1) * (q-1)




e = 65537
found = False
while found == False:
    if math.gcd(e,phi) == 1:
        found = True
    elif math.gcd(e,phi) != 1:
        e += 1
    


# private exponent 
d = pow(e,-1,phi) # modulares inverses
print(f"e{e}")
print(f"n{n}")
 # thats important 



signature = pow(hash_int, d, n)
print(f"signature:{signature}")




verification = pow(signature, e, n)

if verification == hash_int:
    print("signature valid")
else:
    print("signature invalid")




    
   