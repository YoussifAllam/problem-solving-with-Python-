url = input() 
size = len(url)
for i in range(size):
    if url[i] == '?':
        i += 1
        for z in range(i, size):  
            if url[z] == '=':
                print(": ", end="")
                continue
            if url[z] == '&':
                print()
                continue
            print(url[z], end="")
        break