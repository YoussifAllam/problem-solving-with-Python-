
def count_divisors(num):
  m = num // 2
  counter = 0
  for z in range(1, m + 1):
    if num % z == 0:
      counter += 1
  return counter

def is_palindrome(num):
  temp = num
  sum = 0
  while num > 0:
    d = num % 10
    sum = (sum * 10) + d
    num //= 10
  return temp == sum

def main():
  size = int(input())
  arr = [0] * size

  arr= list(map(int,input().split()))

  arr.sort()
  print("The maximum number :", arr[-1])
  print("The minimum number :", arr[0])

  count_prime = 0
  count_palindrome = 0
  for i in range(size):
    if is_palindrome(arr[i]):
      count_palindrome += 1
    m = arr[i] // 2
    flag = 0
    for z in range(2, m + 1):
      if arr[i] % z == 0:
        flag = 1
        break
    if flag == 0 and arr[i] != 1:
      count_prime += 1

  print("The number of prime numbers :", count_prime)
  print("The number of palindrome numbers :", count_palindrome)

  max_divisors = 0
  max_index = 0
  for i in range(size):
    c = count_divisors(arr[i])
    if i == 0:
      max_divisors = c
      max_index = i
    else:
      if c >= max_divisors:
        max_divisors = c
        max_index = i

  print("The number that has the maximum number of divisors :", arr[max_index])

if __name__ == "__main__":
  main()