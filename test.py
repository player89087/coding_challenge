x = 10

x = str(x)
num_left = []
num_right = []
for i in range(0,len(x)):
    num_left.append(x[i])
    num_right.append(x[-i])
    print(num_left,num_right)
    if num_left == num_right:
        print(True)