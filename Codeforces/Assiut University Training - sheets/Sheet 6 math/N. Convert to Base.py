def num(c):
    if c >= '0' and c <= '9':
        return int(c)
    else:
        return ord(c) - ord('A') + 10

def reNum(num):
    if num >= 0 and num <= 9:
        return chr(num + ord('0'))
    else:
        return chr(num + ord('A') - 10)

def toDec(value, base):
    size = len(value)
    power = 1
    result = 0
    for i in range(size - 1, -1, -1):
        result += num(value[i]) * power
        power *= base

    return result

def fromDec(res, base, number):
    index = 0
    while number > 0:
        res[index] = reNum(number % base)
        number //= base
        index += 1
    res[index] = '\0'
    res = res[::-1]
    return res

ca = int(input())
if ca == 1:
    arr ,base =map(int, input().split())
    print(toDec(str(arr), base))
else:
    number, base = map(int, input().split())
    res = [''] * 100
    print(fromDec(res, base, number))