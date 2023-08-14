
def knapSack(W, weight, value, items):
    if W == 0 or items == 0:
        return 0
    if weight[items - 1] > W:
        return knapSack(W, weight, value, items - 1)
    else:
        return max(
            value[items - 1] + knapSack(W - weight[items - 1], weight, value, items - 1), # 90
            knapSack(W, weight, value, items - 1) 
        )

items ,W1 = map(int ,input().split())

weight = []
value = []
for i in range(items):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)
print(knapSack(W1, weight, value, items))