import math

# def find_second_largest(lst):
#     """
#     Finds the second largest element in a list.

#     Args:
#         lst: The input list.

#     Returns:
#         The second largest element in the list, 
#         or None if the list has less than two elements.
#     """
#     if len(lst) < 2:
#         return None

#     largest = max(lst)
#     second_largest = -math.inf 

#     for num in lst:
#         if num > second_largest and num != largest:
#             second_largest = num

#     return second_largest

# # Example usage
# my_list = [10, 5, 20, 3, 15]
# second_largest_num = find_second_largest(my_list)
# print("Second largest element:", second_largest_num)  # Output: Second largest element: 15
second_largest = -math.inf 
print(second_largest )

# def find(x):
#     first_larg=max(x)
#     x.remove(first_larg)
#     second_large=max(x)
#     print("second large number is =",second_large)
    
    

# x=[1,4,3,2,6]
# find(x)