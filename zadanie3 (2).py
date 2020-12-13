def is_divisible(num):
    if num == 1:
        return True

    dividers = [2, 3, 5]
    for div in dividers:
        if num % div == 0:
            return True
    return False


need_index = int(input())
result = 1

i = 0
n = 1
while i != need_index:
    if is_divisible(n):
        result = n
        i += 1
    n += 1
print(result)
