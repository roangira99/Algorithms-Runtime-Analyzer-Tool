from demos import quicksort, merge_sort
import random
import time

def create_random_list(size, max_val): 
    ran_list = [] # create an empty list
    for num in range(size):
        ran_list.append(random.randint(1, max_val)) # append each number to the list
    return ran_list 

size = int(input("What size of list do you want to create? "))
max = int(input("What maximum value do you want for the range? "))

l = create_random_list(size, max)

tic = time.time()
quicksort(l)
toc = time.time()
print(f"Quick sort Elapsed time -> {toc - tic}")

tic = time.time()
merge_sort(l)
toc = time.time()
print(f"Merge sort Elapsed time -> {toc - tic}")


