
import time
import sys

# Task 1

dict1 = {'a':1, 'b':2, 'c':3, 'd':4}
dict2 = {'d':4, 'e':5, 'f':6, 'g':7}

def merg_dictionaries (dict1, dict2):
    start_time = time.time()
    dict3 = dict1 | dict2
    end_time = time.time()
    time_to_complete = end_time - start_time

    print(dict3)
    print(f"Operation completed in {time_to_complete:.7f} seconds.")
    space = sys.getsizeof(dict3)    
    print(f"{space} bytes take for this opertion")

merg_dictionaries(dict1, dict2)

# Task 2

def find_intersection(dict1, dict2):
    start_time = time.time()
    for key1 in dict1:
        for key2 in dict2:
            if key1 == key2:
                print(f"{key1}:{dict1[key1]} from dictionary 1.")
                print(f"{key2}:{dict2[key2]} from dictionary 2.")
    end_time = time.time()
    time_to_complete = end_time - start_time
    print(f"Operation completed in {time_to_complete:.7f} seconds.")

find_intersection(dict1, dict2)

# Task 3
words = ["apple", "giraffe", "ocean", "umbrella", "piano", "mountain", "coffee", "apple", "keyboard", "sunflower", "bicycle", "whisper", "dragonfly", "apple", "chocolate", "telescope", "apple"]



def count_frequency (list, search_word):
    dict1 = {"frequency" : 0}
    counter = 0
    start_time = time.time()

    for word in list:
        if word == search_word:
            counter += 1
            dict1['frequency'] = counter

    print(f"The word {search_word} appears {dict1['frequency']} times in this list.")

    end_time = time.time()
    time_to_complete = end_time - start_time
    print(f"Operation completed in {time_to_complete:.7f} seconds.")
    

count_frequency(words, 'apple')