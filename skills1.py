# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    some_list = some_list[1::2]
    return some_list

all_odd(numbers)

# # Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    some_list = some_list[0::2]
    return some_list

all_even(numbers)

# # Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    temp = []
    for i in word_list:
        word = i
        word_split = len(word)
        if word_split > 4:
            temp = temp + [i]
    return temp

# # Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    first_number = some_list[0]
    for i in some_list:
        x = first_number
        if i < x:
            x = i
    return x

# # Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    temp = 0
    for i in some_list:
        if i < 0:
            temp = i
    return i
    

# # Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    temp = []
    for i in some_list:
        i = float(i)
        i = i / 2
        temp = temp + [i]
    return temp


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    temp = []
    for i in word_list:
        word = i
        word_split = len(word)
        temp = temp + [word_split]

    return temp

# # Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum_list = 0
    for i in numbers:
        sum_list = i + sum_list
    return sum_list


# # Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mult_total = 1
    for i in numbers:
        mult_total = i * mult_total
    return mult_total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    original_string = ""
    for i in string_list:
        original_string = original_string + i
    return original_string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    list_pop = len(numbers)
    list_sum = 0
    for i in numbers:
        list_sum = i + list_sum

    list_avg = list_sum / list_pop

    return list_avg