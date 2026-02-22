import sys 

sys.set_int_max_str_digits(1000000)
prev = 1
prev2 = 0
fib = [0,1]
for i in range(0,200005):
     new = prev + prev2
     prev2 = prev
     prev = new
     fib.append(new)
print((str(fib[199999])))  # bc index 0     

