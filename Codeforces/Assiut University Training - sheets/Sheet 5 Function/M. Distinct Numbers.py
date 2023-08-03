def count_number(array, size):
  count = 1
  for i in range(1, size):
    if array[i] != array[i - 1]:
      count += 1

  return count

def main():
    size = int(input())
    if size == 0:
        print(0)
        return

    array = list(map(int,input().split()))
    array.sort()

    print(count_number(array, size))

if __name__ == "__main__":
  main()