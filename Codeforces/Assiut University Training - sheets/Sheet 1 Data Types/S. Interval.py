x = float(input())
if  0 <= x <= 100:
    
    if  75 <= x <= 100:
        print(f'Interval (75,100]')
    elif  x > int(x):
        print(f'Interval ({int(x)},{int(x+x)}]')
    else:
        print(f'Interval [0,{int(x)}]')
else: print('Out of Intervals')
