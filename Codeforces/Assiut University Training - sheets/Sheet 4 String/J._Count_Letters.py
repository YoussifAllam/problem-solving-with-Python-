s = input()  # read the input string
count = {}   # create an empty dictionary to store the count of each letter

# iterate over each character in the string S
for c in s:
    if c in count:
        count[c] += 1  # if the letter is already in the dictionary, increment its count
    else:
        count[c] = 1   # if the letter is not in the dictionary, add it with count 1

# sort the keys of the dictionary in ascending order and print the counts
for c in sorted(count.keys()):
    print(c, ":", count[c])
