# Remove Duplicates from List (Lists and Loops)
# Write a function remove_duplicates(lst) that removes duplicates
#  from a list while preserving the original order. Do not use sets.
# For example, remove_duplicates([1, 3, 3, 4, 1, 5]) returns [1, 3, 4, 5].
#  Use list methods like append() and a loop to check for duplicates.

def remove_duplicates(lst):
    updated_list = []

    for num in lst:
        if num not in updated_list:
            updated_list.append(num)
    return updated_list


print(remove_duplicates([1, 3, 3, 4, 1, 5]))
