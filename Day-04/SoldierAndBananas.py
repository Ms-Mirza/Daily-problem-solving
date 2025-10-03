# Question link:
# https://codeforces.com/problemset/problem/546/A

# solution 1:

k, n, w = map(int, input().split())

total_price = 0

for i in range(1, w+1):
    total_price += i*k

needed_amount = total_price - n

if(total_price < n):
    print(0)
else:
    print(needed_amount)

# solution 2:

k, n, w = map(int, input().split())

total_price = 0

for i in range(1, w+1):
    total_price += i*k

needed_amount = max(0, total_price - n) # max(a,b) --> returns the larger of a and b.

print(needed_amount)



# solution 3:

k, n, w = map(int, input().split())

total_price = k * w * (w + 1) // 2
needed_amount = max(0, total_price - n)

print(needed_amount)
