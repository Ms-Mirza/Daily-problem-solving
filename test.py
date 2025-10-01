first = (input()).lower() 
second = (input()).lower()

for i in range(len(first)):
    if(first[i]>second[i]):
        print("1")
    elif(first[i]<second[i]):
        print("-1")