sequence = ["11",]

new_num = ""
n = int(input("len: "))

for i in range(1,n):
    prev = str(sequence[i-1])
    count = 0
    print(prev)
    for x in range(1,len(prev)):
        print("hello")
        
        if prev[x] == prev[x-1]:
           count += 1
        
        else: 
            print("test")
            count = str(count)
           
            new_num= count+prev[x]
            sequence.append(new_num)
            new_num = ""
            count = int(count)
            count = 1
            print(sequence)
       