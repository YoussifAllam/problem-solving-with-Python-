n=int(input())

year = int(n / 365) 
month = int((n % 365) /30)
day   =  ((n%365) % 30)
print(year,"years")
print(month,"months") 
print(day ,"days") 











# 400 % 365 == 35