import random 
import math 
import time 
import numpy as np 
start = time.time()
word = "Great job you found the solution [encrypt10n_1s_k3y.html] "


# Generate unicode for the string 
unicode = []
for i in range(0,len(word)): 
    unicode.append(ord(word[i]))


# calculate rsa key pair 

amount = 2**1023
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
power = 1024
for i in range(2):
    is_prime = False
    k = random.randint(0, 10000000) 
    test_num = 2**power + k
    while is_prime == False:
        nums += 1
        if test_num+nums % 2 != 0:
            prime, is_prime, percentage = miller_rabin(test_num+nums, 1000)
        if nums % 100 == 0:
            print(f'checked numbers {nums} \t  nums found {i}')
    p_q.append(test_num +  nums)

print(p_q)

p = p_q[0]
q = p_q[1]

print(f"p,q{p,q}")

n = p * q 
print(f"N{n}") # thats important 
# φ(p⋅q)=(p−1)*(q−1)
phi = (p-1) * (q-1)
print(f"phi{phi}")



e = 2
found = False
while found == False:
    if math.gcd(e,phi) == 1:
        found = True
    elif math.gcd(e,phi) != 1:
        e += 1
    
print(f"e{e}") 

# private exponent 
d = pow(e,-1,phi) # modulares inverses

print(f"d: {d}") # thats important 


#print(f"Unicode list{unicode}")
secret_msg = []
for i in range(0,len(word)):
    secret_msg.append(pow(unicode[i],e,n))
print(f"secret list {secret_msg}")




clear_message = []
for i in range(0,len(secret_msg)):
    clear_message.append(pow(secret_msg[i],d,n))
    print(chr(clear_message[i]))

end = time.time()

print(f"needed time: {end-start}")
print(len(p))