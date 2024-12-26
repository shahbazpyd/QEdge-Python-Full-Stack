def remove_duplicates_sorted(lst):
    """
    Removes duplicates from a sorted list.

    Args:
        lst: The sorted list.

    Returns:
        A new list containing only unique elements.
    """
    if not lst:
        return []  # Handle empty list

    unique_list = [lst[0]]  # Initialize with the first element
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            unique_list.append(lst[i])

    return unique_list

# Example usage
sorted_list = [1, 1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates_sorted(sorted_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]




# def remove_duplcate(x):
#     x.sort()
#     print(x)
#     y=set(x)
#     z=list(y)
#     print(z)

# x=[3,3,4,1,2,5,5]
# remove_duplcate(x)