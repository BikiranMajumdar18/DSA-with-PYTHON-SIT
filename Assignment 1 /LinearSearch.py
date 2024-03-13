''' 1. Write a program of Linear Search. Define a class for LinearList, containing the data members
Lineararray, datatype, and size of the list, and the following methods:
• __init__() initialize the object, it should contain homogeneous data.
• display() display the list of items
• LinearSearch() search the given item
• Inert() insert new item
• Delete delete the specified item '''

class LinearList:
    def __init__(self,arr,dataType=int):
        self.array = arr
        self.size = len(self.array)
        for i in arr:
            if type(i) != dataType:
                print("Error")
                exit()
    def LinearSearch(self,item):
        for i in range(self.size):
            if item == self.array[i]:
                print("item found at ", i , "th index ")
                return i
        else:
                print("item not found ")
    def insert(self,item):
        self.array.append(item)
    def delete(self,delete):
        self.array.remove(delete)
    def display(self):
        print(self.array)
L = LinearList([10,20,52,75,85,78])
L.display()
L.LinearSearch(85)
L.insert(30)
L.delete(85)
