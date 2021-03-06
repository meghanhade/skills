string1 = "I I I I do  not not not not not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27, 99, 125, -99]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7, 99, 125, -99]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "I", "I", "do", "not", "like", "them", "Sam", "I", "am", "zippitydoodah"]

"""

Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	word_list = string1.split()
	word_dictionary = {}
	for word in word_list:
		if word_dictionary.get(word, []):
			word_dictionary[word] += 1
		else:
			word_dictionary[word] = 1
	return word_dictionary
count_unique(string1) 

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	repeating_numbers_list = []
	for number in list1:
		if list2.count(number) >= 1:
			repeating_numbers_list.append(number)
	repeating_numbers_list.sort()
	number_check = repeating_numbers_list[0]
	new_repeating_numbers_list = [repeating_numbers_list[0]]
	for number in repeating_numbers_list:
		if number > number_check:
			number_check = number
			new_repeating_numbers_list.append(number)
	new_repeating_numbers_list.sort()	
	return new_repeating_numbers_list

common_items(list1, list2)

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
	repeating_numbers_dict = {}
	repeating_numbers_list = []
	for number in list1:
		if list2.count(number) >= 1:
			if repeating_numbers_dict.get(number, []):
				repeating_numbers_dict[number] += 1
			else:
				repeating_numbers_dict[number] = 1
	for number in repeating_numbers_dict:
		repeating_numbers_list.append(number)
	repeating_numbers_list.sort()
	return repeating_numbers_list

common_items2(list1, list2)
"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    zero_sum_dict = {}
    for number in list1:
    	pair_number = 0 - number
    	if pair_number in list1:
    		zero_sum_pair_tuple = number, pair_number
    		zero_sum_dict[number] = zero_sum_dict.get(number, zero_sum_pair_tuple)
    zero_sum_pair_list = []
    for number in zero_sum_dict:
    	tuple_pair = zero_sum_dict[number]
    	zero_sum_pair_list.append(tuple_pair)
    return zero_sum_pair_list

sum_zero(list1)


"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
	words_dict = {}
	nonrepeating_list = []
	for word in words:
		if words_dict.get(word, []):
			words_dict[word] += 1
		else:
			words_dict[word] = 1
	for word in words_dict:
		nonrepeating_list.append(word)
	return nonrepeating_list

find_duplicates(words)


"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
# """
# def word_length(words):
    # word_length_dict = {}
    # for word in words:
    # 	letter_tuple = tuple(word)
    # 	# print word, letter_tuple
    # 	letter_list = []
    # 	for letter in letter_tuple:
    # 		letter_list.append(letter)
    # 		print letter_list



    # 		# letter_count = len(letter_list)
    # 	if word_length_dict.get(letter_count):
    # 		# word_length_dict[letter_count] = word
    # 		word_length_dict[letter_count].update({word})
   	# 	else:
   	# 		word_length_dict[letter_count] = word
    # for word_length in word_length_dict:
    # 		print word_length_dict[word_length]
    # print word_length_dict
    	
 

# word_length(words)

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""