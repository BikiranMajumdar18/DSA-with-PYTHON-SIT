''' Write a program of Bubble Sort. Define a class for LinearList, containing the data members
Lineararray, datatype, and size of the list, and the following methods:
• __init__() initialize the object
• display() display the list of items, it should contain homogeneous data.
• BubbleSort() arranged items in ascending order
• Inert() insert new item
• Delete() delete the specified item '''

class LinearList:
    def __init__(self, arr , dataType):
        self.array = arr
        self.size = len(self.array)
        for i in arr:
            if type(i) != dataType:
                print("Error")
                exit()
    def display(self):
        print(self.array)
    def BubbleSort(self):
        for i in range(1,self.size-1):
            c = 0
            for j in range(0,self.size-i):
                if self.array[j] > self.array[j+1]:
                    (self.array[j] , self.array[j+1]) = (self.array[j+1], self.array[j])
                    c = c + 1
            if c == 0:
                break
    def delete(self , item):
        if item in self.array:
            self.array.remove(item)


linear_list = LinearList([4,2,1,5,7,8,12,10,3],int)
linear_list.display()

linear_list.BubbleSort()
linear_list.display()
