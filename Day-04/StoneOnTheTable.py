#Question link:
# https://codeforces.com/problemset/problem/266/A

# solution 1:

num_of_stones = int(input())
stones_data = input()

count = 0

if(len(stones_data) == num_of_stones):
    for i in range(num_of_stones-1):
        if(stones_data[i]==stones_data[i+1]):
            count += 1

    print(count)

else:
    print("Error!!")


# solution 2:

n = int(input())
s = input().strip() # .strip() removes any accidental newline/spaces.

count = sum(a == b for a, b in zip(s, s[1:]))
print(count)
