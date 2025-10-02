# Question link:
# https://codeforces.com/problemset/problem/59/A

#solution 1:

word = input()


upper_case_count = 0

lower_case_count = 0

for char in word:
    if char.isupper():
        upper_case_count += 1
    elif char.islower():
        lower_case_count += 1

if(upper_case_count <= lower_case_count):
    word = word.lower()

else:
    word = word.upper()


print(word)


#solution 2:

word = input()
upper_case_count = sum(char.isupper() for char in word)
# upper_case_count = sum(1 for char in word if char.isupper()) 

if upper_case_count > len(word) // 2:
    print(word.upper())
else:
    print(word.lower())


