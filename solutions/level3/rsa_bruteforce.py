import random 
import math
prime = []

nums = []

for i in range(0,1000): # insert estimated range of p and q 
    nums.append(True)
nums[0] = False
nums[1] = False
for x in range(0,len(nums)):
    if nums[x] == True:
        prime.append(x)
        for y in range(x,len(nums),x):
            nums[y] = False

n = 247483

n_found = False 
#i = 0 
x = 1
p = []
q = []
for i in range(0,100000):
    p.append(random.choice(prime))
    q.append(random.choice(prime))
    if p[0] * q[0] == n:
        n_found = True 
        #print(f"P found: {p} and Q found {q}")
        break
    elif p[0] * q[0] != n:
        p.clear()
        q.clear()

p_num = p[0]
q_num = q[0]
phi = (p_num-1) * (q_num-1)

e = 2
found = False
while found == False:
    if math.gcd(e,phi) == 1:
        found = True
    elif math.gcd(e,phi) != 1:
        e += 1

d = pow(e,-1,phi) # modulares inverses

print(f"d: {d}") 

secret_msg =  [110428, 244129, 40369, 170224, 75998, 32768, 201084, 130216, 198743, 32768, 39180, 130216, 116715, 32768, 71276, 130216, 116715, 93585, 10068, 32768, 75998, 134932, 40369, 32768, 35977, 130216, 22297, 116715, 75998, 167693, 130216, 93585, 32768, 11122, 40369, 93585, 227850, 244129, 39180, 167513, 75998, 117649, 110592, 93585, 114926, 117649, 35977, 114926, 235111, 132651, 39180, 97336, 134932, 75998, 57614, 22297, 61908, 32768]
clear_message = []
for i in range(0,len(secret_msg)):
    clear_message.append(pow(secret_msg[i],d,n))
    print(chr(clear_message[i]),end="")
