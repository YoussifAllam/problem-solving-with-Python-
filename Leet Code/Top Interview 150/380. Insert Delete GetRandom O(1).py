import random
class RandomizedSet:

    def __init__(self):
        self.RandomizedSet = [[], [1], [2], [2], [], [1], [2], []]


    def insert(self, val: int) -> bool:
        if val not  in self.RandomizedSet:
            self.RandomizedSet.append(val)
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:

        if val  in self.RandomizedSet:
            self.RandomizedSet.pop()        
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        index= random.randint(0 , len(self.RandomizedSet)-1)
        return self.RandomizedSet[index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(2)
print(obj.RandomizedSet)
param_2 = obj.remove(2)
param_4 = obj.insert(2)
param_2 = obj.remove(3)
param_3 = obj.getRandom()
print(param_1,param_2,param_3,param_4)

'''my_set = {1, 2, 3,3}
my_set.add(3)
print(my_set)'''