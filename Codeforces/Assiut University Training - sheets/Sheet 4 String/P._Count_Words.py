sen = input()
res = ""
counter = 0
for i in range(len(sen)):
  if sen[i] not in " !.,?":
    res += sen[i]

  if (sen[i] in " !.,?" or i == len(sen) - 1) and res != "":
    counter += 1
    res = ""
print(counter)