a, b = map(int, input().split())

# Initialize a list to store lucky numbers
lucky_nums = []

# Iterate over the range [A, B] and check if each number is lucky
for num in range(a, b+1):
    if all(digit in ['4', '7'] for digit in str(num)):
        lucky_nums.append(num)

# Check if there are any lucky numbers and print them
if len(lucky_nums) > 0:
    print(' '.join(str(num) for num in lucky_nums))
else:
    print('-1')
