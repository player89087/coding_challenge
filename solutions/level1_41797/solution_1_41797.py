import sys 

sys.set_int_max_str_digits(1000000)

a = 1
def hanoi(n):
    a = 2**n - 1 
    return a 
print(len(str(hanoi(500000)))) 