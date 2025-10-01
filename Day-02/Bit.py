
x = 0
for _ in range(int(input())):
    bit = input()
    
    if(bit == "X++" or bit == "++X"):
        x += 1
    elif(bit == "X--" or bit == "--X"):
        x -= 1
    else:
        continue

print(x)
    
