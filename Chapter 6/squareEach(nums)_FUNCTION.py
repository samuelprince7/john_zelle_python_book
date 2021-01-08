# this fuction updates a list of numbers (nums_list)
# by squaring each number in the list, and returning that result
# mainly demonstrates how fuctions can be used to
# update the value of lists because, lists are mutable
# includes a useful for loop for this feature

def squareEach(nums_list):
    for i in range(len(nums_list)):
        nums_list[i] = nums_list[i] ** 2

    #returns the mutated list based on calling the function squareEach
    # often times, you do not necessarily need to author the logic of 
    # a section of code in order to wrap it into a fuction
    # this can increase your abilities as a coder by working
    # in tandem with the logic authored by others as well
    return nums_list 

print(squareEach([7, 5, 12]))
print(squareEach([5, 2, 3]))
print(squareEach([5, 10, 20, 40]))