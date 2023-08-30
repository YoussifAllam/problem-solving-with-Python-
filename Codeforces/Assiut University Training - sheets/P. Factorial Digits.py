import math

def count_digits_in_factorial(num):


  result = 0
  for i in range(2, num + 1):
    result += math.log10(i)

  return int(result) + 1


if __name__ == "__main__":
  num = int(input())
  print("Number of digits of {}! is {}".format(num, count_digits_in_factorial(num)))