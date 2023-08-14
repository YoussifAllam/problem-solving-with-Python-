str1 = input()

Vowel_letters = ['a', 'e', 'i', 'o', 'u']
c = 0
i = len(str1)-1
def recursion( i , str1: str , v) :
    global c
   # print(i,"  " , str1[i])
    if i >-1:
        if str(str1[i].lower()) in Vowel_letters :
            c+=1
        recursion( i-1 , str1,v ) 

    

recursion(i,str1,Vowel_letters)
print(c)


