# Question link:
# https://codeforces.com/problemset/problem/263/A

matrix = []

locate_row = 0

locate_col = 0

for i in range(5):
    row = list(map(int,input().split()))
    matrix.append(row)
    for j in range(5):
        if row[j] == 1:
            locate_row = i
            locate_col = j

moves = abs(locate_row - 2) + abs(locate_col - 2)

print(moves)


 
