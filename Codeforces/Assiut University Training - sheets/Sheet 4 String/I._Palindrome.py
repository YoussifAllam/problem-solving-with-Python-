s=input()
str1 = ""
def reverse(s):
    global str1
    for i in s:
        str1 = i + str1
reverse(s)
if s == str1:
    print("YES")
else:
    print("NO")