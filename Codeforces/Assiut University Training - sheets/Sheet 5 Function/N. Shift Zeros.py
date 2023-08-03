def shift_zeros(array):


    count_of_non_zero_elements = 0
    for element in array:
        if element != 0:
            array[count_of_non_zero_elements] = element
            count_of_non_zero_elements += 1
    for i in range(count_of_non_zero_elements, len(array)):
        array[i] = 0
    return array



n = int(input())
array = list(map(int, input().split()))
array = shift_zeros(array)
print(*array)

