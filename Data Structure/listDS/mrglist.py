def merge_sorted_lists(list1, list2):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        list1: The first sorted list.
        list2: The second sorted list.

    Returns:
        A new list containing the merged and sorted elements.
    """
    merged_list = []
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from list1 (if any)
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append remaining elements from list2 (if any)
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]





# def mrglist(x,y):
#     x.sort()
#     y.sort()
#     z=x+y
#     print(z)
    

# x=[4,2,5,1,3]
# y=[10,6,9,8,7]
# mrglist(x,y)