size = int(input())

arr = [0] * size
arr2 = [0] * size

arr0 = list( map( int , input().split() ) )
arr = arr0
arr2 = arr0

temp = 0
counter = 0
temp2 = 0
counter2 = 1

arr2[0] *= -1

for i in range(size):
    if i == 0:
        temp = arr[i]
        temp2 = arr2[i]
    else:
        if (temp > 0 and arr[i] > 0) or (temp < 0 and arr[i] < 0):
            arr[i] *= -1
            counter += 1
        if (temp2 > 0 and arr2[i] > 0) or (temp2 < 0 and arr2[i] < 0):
            arr2[i] *= -1
            counter2 += 1
        temp = arr[i]
        temp2 = arr2[i]

print(min(counter, counter2))