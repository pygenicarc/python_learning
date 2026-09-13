'''
lst = [1, 2, 3, 4, 5, 'subbu', 'hello', 6, 7, 8, 9, 10]
test = [1,2,3,4]

# formatting the list to print only the first 5 elements
print('elements of the list: {0}, elements: {1}'.format(lst, test))
print(f'elements of the list: {lst}, elements: {test}')
'''
'''
lst = [1, 2, 3, 4, 5]
print(lst[0])  # prints the first element of the list
lst[0] = 10  # changes the first element of the list to 10
print(lst)  # prints the updated list
lst.append(6)  # adds 6 to the end of the list
print(lst)  # prints the updated list
lst.extend([10, 20, 30])  # adds multiple elements to the end of the list
print(lst)  # prints the updated list
lst.remove(10)  # removes the first occurrence of 10 from the list
print(lst)  # prints the updated list
lst.pop()  # removes the last element from the list
print(lst)  # prints the updated list
lst.pop(1)  # removes the element at index 1 from the list
print(lst)  # prints the updated list
print(len(lst))  # prints the length of the list
'''
'''
lst = [1, 20, 30, 40, 5, 0, 2, 60]
lst.sort()  # sorts the list in ascending order
print(lst)  # prints the sorted list
lst1  = [1, 20, 30, 40, 5, 0, 2, 60]
lst.sort(reverse=True)  # sorts the list in descending order
print(lst)  # prints the sorted list
'''

lst = [1, 20, 30, 40, 5, 0, 2, 60]
for i in lst:
    print(i)  # prints each element of the list

'''
num = 10

for i in num:
    print(i)  # prints each digit of the number
'''
test = 'hello'

for i in test:
    print(i)  # prints each character of the string
