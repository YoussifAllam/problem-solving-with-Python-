import sys

def max_path(row, column, arr):

  if row == len(arr) - 1 and column == len(arr[0]) - 1:
    return arr[row][column]
  elif row == len(arr) or column == len(arr[0]):
    return -sys.maxsize

  right = max_path(row, column + 1, arr)
  down = max_path(row + 1, column, arr)
  return arr[row][column] + max(right, down)

def main():
  row, column = list(map(int, input().split()))
  arr = []
  for _ in range(row):
    arr.append(list(map(int, input().split())))

  print(max_path(0, 0, arr))

if __name__ == "__main__":
  main()