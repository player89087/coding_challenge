n = 1333
d = 1031

secret_msg = [787, 1183, 504, 487]
clear_message = []
for i in range(0,len(secret_msg)):
    clear_message.append((int(secret_msg[i]) ** d) % n)
    print(chr(clear_message[i]))

