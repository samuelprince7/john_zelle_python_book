# a function that returns the sum of the numbers in the list

def sumList(nums_list):
    total = 0
    for i in range(len(nums_list)):
        total = nums_list[i] + total
    # SLP authorded the logic of this function
    return total

print(sumList([7, 5, 12]))
print(sumList([5, 2, 3]))
print(sumList([5, 10, 20, 40]))