lst_even = []
lst_odd = []
def even_odd(lst):
    for num in lst: # 0,1,2,3,4,5,6
        if num % 2 == 0:
            lst_even.append(num)
        else:
            lst_odd.append(num)
    return lst_even, lst_odd
result_even, result_odd = even_odd([1,6,7,8,9,10])
print(f"Even numbers: {result_even}")
print(f"Odd numbers: {result_odd}")