# summing of numbers function
def sum_large_numbers():
    total = 0
    for i in range(1000000):
        total += i
    return total
# add function
def add():
    x, y = 500000, 1000000
    resulting_sum = 0
    resulting_sum += x
    resulting_sum += y
    return resulting_sum

# star triangle function
def star_triangle():
    n = 100
    result = ""
    for i in range(1, n + 1):
        for j in range(i):
            result += "*"
        result += "\n"
    return result
