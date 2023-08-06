Key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
Original = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
flag = int(input())
value = input() 
# 01234
# "Egypt"   ['E','g','y','p','t']
size = len(value)
z = 0
if flag == 1:
    for i in range(size):
        for z in range(len(Original)):
            if value[i] == Original[z]: #  E == E
                break
        print(Key[z], end="")
else:
    for i in range(size):
        for z in range(len(Key)):
            if value[i] == Key[z]: #  E == E
                break
        print(Original[z], end="")