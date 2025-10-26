from decimal import * 
numb = int(input("Amount: "))
prev = 1
prev2 = 0
new = 0 
for i in range(0,numb):
    new = prev + prev2
    if i == numb -1 : 
         golden_ratio = Decimal(new) / Decimal(prev) # relationship between two sections
    prev2 = prev
    prev = new
    

