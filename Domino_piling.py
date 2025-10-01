# Question link: 
# https://codeforces.com/problemset/problem/50/A?__cf_chl_tk=_5qSqDFRew7C4fgVsc27IQKLyomeDzUvUKlmB60caFg-1759255540-1.0.1.1-goNtaaQDfWzt_5UgmpI0PJotMxjVlCdcQqxGb7HTKRo

#input board size:
M, N = map(int, input().split())



board_area = M * N

domino_piece_size = 2*1

max_num_of_dominos = board_area // domino_piece_size
print(max_num_of_dominos)