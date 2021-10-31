""" Task algorithms
    - binary search
    - quick sort(iterative)
    - recursive factorial implement"""


def binary_search(array: list, num: int) -> int:
    """Binary search.
     Return _binary search"""
    low = 0
    high = len(array) - 1
    return _binary_search(array, low, high, num)


def _binary_search(array: list, low: int, high: int, num: int) -> int:
    """Recursive binary search.
    Return index of num in arr if present, else -1"""
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If num found
        if array[mid] == num:
            return mid
        # If element is smaller than mid, element in left sub array
        if array[mid] > num:
            return _binary_search(array, low, mid - 1, num)
        # Else the element in right sub array
        return _binary_search(array, mid + 1, high, num)
    # If no such element in the array
    return -1


def quick_sort_iterative(array: list):
    """Quick sort iterative method
        Return sorting array"""
    # Check if list consist 1 element or empty
    if len(array) < 2:
        return array
    # low, high - starting and ending indexes
    low, high = 0, len(array) - 1
    # Create stack of [0, 0, ....]
    size = high - low + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of low and high to stack
    top += 1
    stack[top] = low
    top += 1
    stack[top] = high

    # keep popping from stack while is not empty
    while top >= 0:
        # pop high and low
        high = stack[top]
        top -= 1
        low = stack[top]
        top -= 1

        # set pivot element at its correct position in sorted array
        # Call partition func
        part = partition(array, low, high)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if part - 1 > low:
            top += 1
            stack[top] = low
            top += 1
            stack[top] = part - 1
        # If there are elements on right side of pivot,
        # then push right side to stack
        if part + 1 < high:
            top += 1
            stack[top] = part + 1
            top += 1
            stack[top] = high


def partition(array: list, low: int, high: int):
    """Partitioning loop for quick sort method"""
    i = low - 1
    temp = array[high]
    for j in range(low, high):
        if array[j] <= temp:
            # increment index of smaller element
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def recursion_factorial(num: int) -> int:
    """Check num and call _recursion_factorial"""
    if isinstance(num, int):
        return _recursion_factorial(num)
    raise TypeError("Number must be integer")


def _recursion_factorial(num: int) -> int:
    """Count factorial of a numbers using recursion"""
    if num == 1:
        return num
    return num * recursion_factorial(num - 1)
