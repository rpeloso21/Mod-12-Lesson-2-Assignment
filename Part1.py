# Task 1
import time
import sys

def square_number (n):
    start_time = time.time()
    squares = [i**i for i in range(1, n)]
    end_time = time.time()
    time_to_complete = end_time - start_time
    for number in squares:
        print(f"- {number} \n")
    print(f"Operation completed in {time_to_complete:.7f} seconds.")
    space = sys.getsizeof(squares)    
    print(f"{space} bytes take for this opertion")

square_number(1000)

# Task 2

def reverse_sub_list (i, j, n):
    start_time = time.time()
    squares = [i**i for i in range(1, n)]
    sub = squares[i:(j+1)]
    sub.reverse()
    end_time = time.time()
    time_to_complete = end_time - start_time
    print(sub)
    print(f"Operation completed in {time_to_complete:.7f} seconds.")
    space = sys.getsizeof(sub)    
    print(f"{space} bytes take for this opertion")

reverse_sub_list(15, 20, 100)

# Task 3

list1 = [i**i for i in range(1, 20)]
list2 = [i**2 for i in range(10, 20)]

def merge_and_sort (list1, list2):
    start_time = time.time()
    list3 = list1 + list2
    list3.sort()
    end_time = time.time()
    time_to_complete = end_time - start_time
    print(list3)
    print(f"Operation completed in {time_to_complete:.7f} seconds.")
    space = sys.getsizeof(list3)    
    print(f"{space} bytes take for this opertion")


merge_and_sort(list1, list2)