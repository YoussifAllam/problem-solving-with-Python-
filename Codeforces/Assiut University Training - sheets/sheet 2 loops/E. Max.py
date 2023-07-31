n=int(input())
heights=list(input().split())
heights=[int(i) for i in heights]


largest_number = heights[0]

for number in heights:
    if number > largest_number:
        largest_number = number

print(largest_number)


