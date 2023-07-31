def main():
    counter = int(input())
    res = []
    for _ in range(counter):
        num1, num2 = map(int, input().split())
        if num1 * (num1 + 1) // 2 < num2:
            print(-1)
        else:
            sum = 0
            for z in range(num1, 0, -1):
                if sum + z <= num2:
                    sum += z
                    res.append(z)
                if sum == num2:
                    break

    for x in range(len(res)):
        print(res[x], end=" ")
    print()


if __name__ == "__main__":
    main()