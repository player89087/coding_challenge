import random 
import math 
word = "Great job you found the solution [encrypt10n_1s_k3y.html] "


# Generate unicode for the string 
unicode = []
for i in range(0,len(word)): 
    unicode.append(ord(word[i]))


# calculate rsa key pair 

amount = 50
prime_numb = []
for i in range(2,amount):
    is_prime_number = True 
    for x in prime_numb:
        if i % x == 0:
            is_prime_number = False
            break
       
    
    if is_prime_number == True:
        prime_numb.append(i)  

p = random.choice(prime_numb)
q = random.choice(prime_numb)

print(f"p,q{p,q}")

N = p * q 
print(f"N{N}") # thats important 
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


print(f"Unicode list{unicode}")
secret_msg = []
for i in range(0,len(word)):
    secret_msg.append((unicode[i] ** e) % N)
print(f"secret list {secret_msg}")




clear_message = []
for i in range(0,len(secret_msg)):
    clear_message.append((int(secret_msg[i]) ** d) % N)
    print(chr(clear_message[i]))

