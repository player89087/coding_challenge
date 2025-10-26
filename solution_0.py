import sys 

sys.set_int_max_str_digits(100000)
numb = 200000
prev = 1
prev2 = 0
new = 0 
for i in range(0,200000):
     new = prev + prev2
     prev2 = prev
     prev = new
     
new = str(new)        
print(len(new))
