def main():
    size = int(input())
    value = input()
    temp = value[0]
    counter = 1
    for i in range(1, size):
        if value[i] != temp:
            counter += 1
            temp = value[i]
    print(counter)

if __name__ == "__main__":
    main()