#Question link:
#https://codeforces.com/problemset/problem/231/A

num_of_problem = int(input())
count = 0

for i in range(1, num_of_problem+1):
    p, v, t = map(int,input().split())
    if((p==1 and v==1) or (p==1 and t==1) or (t==1 and v==1)):
        count+=1
    else:
        continue

print(count)
