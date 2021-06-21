# work with these variables
eugene = set(input().split())
rose = set(input().split())

diff_1 = eugene.difference(rose)
diff_2 = rose.difference(eugene)
print(diff_1 | diff_2)
