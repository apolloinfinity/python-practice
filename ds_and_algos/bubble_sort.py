def bubble_sort(arr):
    '''
    Bubble Sort is one of the simpler sorting algos. Because it uses two for loops and one of them being
    nested, the time complexity is O(n**2). 
    It's useful for small datasets but it wouldn't be efficient for larger data sets.
    Bubble sort is also a stable sort. It means it dnoes not disturb sequences other than the one being specified. 
    '''
    list_length = len(arr) - 1
    for i in range(list_length): # Outer loop controls how many iterations this algo will make

        for j in range(list_length): # All the comparisons will be done with the inner loop

            if arr[j] > arr[j + 1]: # if the current inner-loop iteration is bigger than the next item in the list, 

                arr[j], arr[j + 1] = arr[j + 1], arr[j] # then swap the numbers via Python's tuple unpacking(comma operator?)

    return arr # Once all the swapping is done, return the sorted list.


a_list = [32, 6, 9, 1]

print(bubble_sort(a_list))