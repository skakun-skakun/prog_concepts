a = list(map(int, input().split()))
print(a)

# -----------------------------------

# Task 1
print((lambda lst, x, y, *args: [i for i in lst if i % x == 0 and i % y != 0])(a, *map(int, input().split())))

# Task 2

# Task 3

# Task 4

# Task 5

# Task 6

# Task 7

# Task 8

# Task 9

# Task 10
print((lambda lst, x, y, *args: [(i, i*y)[i > x] for i in lst])(a, *map(int, input().split())))
