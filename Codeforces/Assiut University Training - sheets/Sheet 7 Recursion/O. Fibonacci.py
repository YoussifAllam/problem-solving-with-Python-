def process(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return process(num - 1) + process(num - 2)


num = int(input())
print(process(num))

