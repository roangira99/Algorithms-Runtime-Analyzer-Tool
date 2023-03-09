from demos import quicksort, merge_sort, bubble_sort
import random
import time

def create_random_list(size, max_val): 
    ran_list = [] # create an empty list
    for num in range(size):
        ran_list.append(random.randint(1, max_val)) # append each number to the list
    return ran_list 

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")  # The dunder method gives you just the name of the function instead of the string representation of the object
    # :.5f takes the value in the seconds variable and limits it to 5 decimal places

size = int(input("What size of list do you want to create? "))
max = int(input("What maximum value do you want for the range? "))
run_times = int(input("How many times do you want to run? "))

for num in range(run_times):
    print(f"Run {num+1}")
    l = create_random_list(size, max)
    # analyze_func(bubble_sort, l.copy()) # the l.copy method ensures bubble sort doesn't sort the original list (sorting the list in place)
    analyze_func(quicksort, l) # the first argument passes in the function as an object to analyze_func
    # analyze_func(merge_sort, l) 
    analyze_func(sorted, l)
    print("-" * 50)

