c = input()

code = ord(c)

next_code = code + 1

if next_code == 123:
    next_code = 97

next_char = chr(next_code)

print(next_char)