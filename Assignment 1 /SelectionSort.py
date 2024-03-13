''' 3. Write a program of Linear Sort. Define a class for LinearList, containing the data members
Lineararray, datatype, and size of the list, and the following methods:
• __init__() initialize the object, it should contain homogeneous data.
• display() display the list of items
• SelectionSort() arranged items in ascending order
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
    def Selection_Sort(self):
        for i in range(self.size):
            for k in range(i+1,self.size):
                if self.array[i] > self.array[k]:
                    (self.array[i] , self.array[k]) = (self.array[k] , self.array[i])
    def delete(self , item):
        if item in self.array:
            self.array.remove(item)

linear_list = LinearList([4,2,1,5,7,8,12,10,3],int)
linear_list.display()

linear_list.Selection_Sort()
linear_list.display()

        
