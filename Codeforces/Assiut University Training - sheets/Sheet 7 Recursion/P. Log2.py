
counter = 0
def log(num): # 8
    global counter
    if num == 1:
        return 0
    counter += 1 # 3
    log(num//2) # 1

num = int(input())
log(num)
print(counter)