# Question link:
# https://codeforces.com/problemset/problem/339/A

# solution 1: (time complexity: O(n log n).)

s = input()

s1 = s.replace("+","")  # removes all '+' signs

sum_order = "+".join(sorted(s1)) # sorts digits and joins with '+'

print(sum_order)






# # solution 2: (time complexity: O(n).)

# s = input().split('+') # each number is a separate element in a list, which is easier to manipulate (count, sort, etc.).
# count1 = s.count("1")
# count2 = s.count("2")
# count3 = s.count("3")

# result = "+".join(["1"]*count1 + ["2"]*count2 + ["3"]*count3)
# print(result)
