n,m=map(int,input().split())
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
def is_subsequence(N, M, A, B):
    i = 0  # index to iterate over A
    j = 0  # index to iterate over B
    while i < N and j < M:
        if A[i] == B[j]:
            j += 1
        i += 1
    if j == M:
        print("YES")
    else:
        print("NO")

is_subsequence(n,m,list1,list2)

