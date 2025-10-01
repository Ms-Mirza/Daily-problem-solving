#question link:
# https://codeforces.com/problemset/problem/71/A

test_case = int(input())
while(test_case>0):
    string = input()
    length = len(string)
    if(length>10):
        mid = length - 2
        start = string[0]
        end = string[-1]
        print(f"{start}{mid}{end}")

    else:
        print(string)

    test_case-=1

    

# other solution:

# for _ in range(int(input())):
#     word = input()
#     if len(word) > 10:
#         print(f"{word[0]}{len(word)-2}{word[-1]}")
#     else:
#         print(word)
