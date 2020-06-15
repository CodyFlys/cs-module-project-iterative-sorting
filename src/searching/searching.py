def linear_search(arr, target):
    # basic loop over arr
    for i in range(0, len(arr)):
        # check if arr index of our loop currently matches target if so return i
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # set the low to 0
    low = 0
    # set the high to the arr length
    high = len(arr)

    while True:
        # make a variable called middle and set it to be the low (0) and high (arr length) divided by 2. AKA the middle.
        middle = round((low + high) / 2)
        # check if high is less than the low or middle is greater than the length of the array
        if high < low or middle >= len(arr):
            return -1
        # set current to equal the array at the middle variables index. aka the middle.
        current = arr[middle]

        # check if target == current if so return middle.
        if target == current:
            return middle
        elif target < current:
            # if the target is less than the current (middle) set the high variable not to the array length but rather the middle. because we know the right side is now useless and only need the left.
            high = middle
        else:
            # else set the low variable to middle + 1
            low = middle + 1


    return -1  # not found
