print("Algorithms file loaded")

def quicksort(arr):
    if len(arr) < 2: # base case
        return arr
    else:
        pivot = arr[-1] # in this case the pivot is the last element
        smaller, equal, larger = [], [], []
        for num in arr:
            if num < pivot:
                smaller.append(num) # append to smaller list
            elif num == pivot:
                equal.append(num) # append to equal list
            else:
                larger.append(num) # append to larger  list
        # recursively run the quicksort function on the smaller and larger lists to get a fully sorted list
        return quicksort(smaller) + equal + quicksort(larger) # concatenating the three objects returns a single list instead of three separate lists in tuple format

def merge_sorted(arr1,arr2): # takes in two sorted lists
    sorted_arr = []
    i, j = 0, 0 # indices i & j used to iterate through the two lists
    while i < len(arr1) and j < len(arr2): # breaks out of program when we get to the end of one of the lists
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1 # move index by 1 if an append occurs
        else:
            sorted_arr.append(arr2[j])
            j += 1
    # Grab the value that is less than the length of the array it is working with and paste any elements that are remaining
    while i < len(arr1):
        sorted_arr.append(arr1[i]) # copy the remaining items to the end
        i += 1 

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = merge_sort(arr[:middle])
        l2 = merge_sort(arr[middle:])
        return merge_sorted(l1, l2)
    
def bubble_sort(arr):
    swap_happened = True # Flag that checks whether a swap happened
    while swap_happened:
        swap_happened = False
        # the loop should go to the lastElement - 1 because after the lastElement there is nothing to compare with
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num] # Dynamic swapping
