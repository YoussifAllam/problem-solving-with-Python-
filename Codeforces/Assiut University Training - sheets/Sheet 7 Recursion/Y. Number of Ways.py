
num1 ,num2 = map(int,input().split()) # 2


def way(number):
  if number >= num2:
    return int(number == num2)
  return way(number + 1) + way(number + 2) + way(number + 3)


print(way(num1))