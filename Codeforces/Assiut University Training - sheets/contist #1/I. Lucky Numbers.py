def main():
  num = input()
  num1 = int(num[0])
  num2 = int(num[1])
  if num2 == 0:
    print("YES")
  else:
    if num1 % num2 == 0 or num2 % num1 == 0:
      print("YES")
    else:
      print("NO")

if __name__ == "__main__":
  main()