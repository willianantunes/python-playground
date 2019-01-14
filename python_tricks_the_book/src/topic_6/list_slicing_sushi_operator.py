lst = [1, 2, 3, 4, 5]
# lst[start:end:step]
print(lst[1:3:1])  # [2, 3]
print(lst[1:3:2])  # [2]
print(lst[1:4:2])  # [2, 4]
print(lst[::2])  # [1, 3, 5]

# With [::-1] slice, you'll get a copy of the original list, but in reverse order
print(lst[::-1])  # [5, 4, 3, 2, 1]
lst.reverse()  # better than ::-1
print(lst)

# You can use : operator to clear all elements from a list  without destroying the list object itself
lst = [1, 2, 3, 4, 5]
del lst[:]
print(lst)

lst = [1, 2, 3, 4, 5]
lst.clear()
print(lst)  # better than :

lst = [1, 2, 3, 4, 5]
original_list = lst
lst[:] = [7, 8, 9]
print(lst)  # [7, 8, 9]
print(original_list)  # [7, 8, 9]
print(original_list is lst)  # True

copied_list = lst[:]  # shallow copy
print(copied_list is lst)  # False
