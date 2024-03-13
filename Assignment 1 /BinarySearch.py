''' Write a program of Binary Search. Define a class for LinearList, containing the data members
Lineararray, datatype, and size of the list, and the following methods:
• __init__() initialize the object, it should contain homogeneous data.
• display() display the list of items
• BinarySearch() search the given item, items should be in sorted order
• Insert() insert new item 
• Delete delete the specified item '''


class LinearList:
    def __init__(self, linear_array, data_type):
        self.linear_array = linear_array
        self.data_type = data_type

    def display(self):
        print("Linear Array:", self.linear_array)

    def binary_search(self, item):
        low = 0
        high = len(self.linear_array) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.linear_array[mid] == item:
                return mid
            elif self.linear_array[mid] < item:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def insert(self, item):
        if isinstance(item, self.data_type):
            if len(self.linear_array) == 0 or item >= self.linear_array[-1]:
                self.linear_array.append(item)
            else:
                for i in range(len(self.linear_array)):
                    if item < self.linear_array[i]:
                        self.linear_array.insert(i, item)
                        break
        else:
            print("Invalid data type for insertion.")

    def delete(self, item):
        if item in self.linear_array:
            self.linear_array.remove(item)
        else:
            print("Item not found in linear array.")

# Example usage
linear_list = LinearList([1, 2, 4, 5, 6, 7], int)
print("Original:")
linear_list.display()

item_to_search = 4
index = linear_list.binary_search(item_to_search)
if index != -1:
    print(f"\n{item_to_search} found at index {index}.")
else:
    print(f"\n{item_to_search} not found.")

linear_list.insert(3)
print("\nAfter Inserting 3:")
linear_list.display()

linear_list.delete(5)
print("\nAfter Deleting 5:")
linear_list.display()
