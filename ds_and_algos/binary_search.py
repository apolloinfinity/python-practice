def binary_search(a_list, target):
    '''
    Binary search works on the premise of divide & conquer.
    It works best if the list or array is sorted. 
    '''
    # get the first and last indexes of the array 
    first = 0 # first index of list
    last = len(a_list) -1 # last index of list
    
    # keep running the while loop as long as last is larger than the first index of each iteration
    while last >= first:
        # must find the midpoint index of the list by dividing it and flooring it.
        mid = (first + last) // 2

        if a_list[mid] == target:
            '''
            Depending on what you want returned, you can return 'True' 
            if the item exists in the list or return 'mid' to return
            the index of the item found.
            '''
            return mid
        else:
            # if the target is less than the mid, set a new ending index
            # this also drops the left half of the array
            if target < a_list[mid]:
                last = mid - 1
                
            else:
            # else set new first index on whats left of the array
            # this one drops the right half of the array
                first = mid + 1
               
    return False



my_list = [1,2,3,4,5,6]
print(binary_search(my_list, 4)) # should return True or 3 if returning the index
