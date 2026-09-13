# a = 100
# b = 200
# sum = a + b
# print("The sum of a and b is:", sum)  # prints the sum of a

def add_numbers(x=0, y=0, *args):  # defines a function that takes two arguments, x and y, with a default value of 0 for y
    sum = x + y
    print("args:", args)  # prints the values of the arguments passed to the function
    for i in args:  # iterates through the values of the arguments passed to the function
        print("sum:", sum)  # prints the current value of sum
        print("i:", i)  # prints the value of the current argument
        sum = sum + i
    return sum


sum = add_numbers(1,2,3,4,5,6,)  # calls the add_numbers function and stores the result in sum
print("The sum of all the numbers is:", sum)  # prints the sum of all the numbers
