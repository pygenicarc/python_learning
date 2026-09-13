lst = [1,2,3,4,5] # it is mutable
lst[0] = 10
print(lst)  # prints the updated list

numbers = (1, 2, 3, 4, 5)
print(numbers)  # prints the tuple
print(numbers[0])  # prints the first element of the tuple
numbers[0] = 10  # raises an error because tuples are immutable

