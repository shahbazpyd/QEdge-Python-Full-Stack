def reverse_list_in_place(lst):
    """
    Reverses the given list in-place.

    Args:
        lst: The list to be reversed.
    """
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]  # Swap elements
        start += 1
        end -= 1

# Example usage
my_list = [1, 4, 3, 2, 5]
reverse_list_in_place(my_list)
print(my_list)  # Output: [5, 4, 3, 2, 1]




# def reverse_list(x):
#     print(x)
#     revlist=x[::-1]
#     return revlist

# x= [10,20,30,40,50]
# final_list=reverse_list(x)
# print(final_list)






# def reverse_list(x):
#     print(x)
#     x.reverse()
#     return x

# x= [10,20,30,40,50]
# final_list=reverse_list(x)
# print(final_list)






# def reverse_list(x):
#     print(x[::-1])
  
# x= [10,20,30,40,50]
# reverse_list(x)




# def revlist(x):
#     x.sort(reverse=True)
#     return x
    

# x=[3,7,3,7,9,5,4]
# z=revlist(x)
# print(z)


# def even(n):
#     print([p for p in range(1,n) if p%2==0])
# n=int(input("enter number of range"))
# even(n)

