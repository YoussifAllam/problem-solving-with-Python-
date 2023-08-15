def is_power_of_2(n):
  if n == 0:
    return False

  while n % 2 == 0:
    n = n // 2

  return n == 1

def main():
  n = int(input())

  if is_power_of_2(n):
    print("YES")
  else:
    print("NO")

if __name__ == "__main__":
  main()

'''
def is_power_of_2_2(n):
  import math as m 
  res = m.log(n) / m.log(2)
  
  return res.is_integer
'''