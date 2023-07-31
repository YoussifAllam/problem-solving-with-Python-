t = int(input())  # number of test cases

for _ in range(t):
    n = int(input())  # number of bags
    a = list(map(int, input().split()))  # candies in each bag

    # separate the bags with even and odd candies
    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 == 1]

    # sort the even bags in decreasing order and odd bags in increasing order
    even.sort(reverse=True)
    odd.sort()

    # calculate the total candies of Mihai and Bianca
    mihai = sum(even)
    bianca = sum(odd)

    # check if Mihai always has more candies than Bianca
    if mihai > bianca:
        print("YES")
    else:
        print("NO")
