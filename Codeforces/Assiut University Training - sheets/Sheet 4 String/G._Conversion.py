s=input()

for i in s:
    if i !=",":
        if i.islower():
         print(i.upper(),end="")
        else:
         print(i.lower(),end="")
    else:
        print(" ",end="")


    