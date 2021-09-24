from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	random.seed(seed)
	arr=[num for num in range(number)]
	# print(array)
	random.shuffle(arr)
	# print(array)
	return arr

# print(gen_random_int(15,20))

def generate():
	global array
	number = 10
	seed = 200

	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	array = gen_random_int(number,seed)
	
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = ""
	for num in array:
		num_str=str(num)
		array_str=array_str+","+num_str
	array_str=array_str+"."
	array_str=array_str[1:]
	# return array_str
	
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str

# print(generate())

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	array_new=array[:]
	print(array_new)
	array_sort=sort_func(array_new)
	array_str = ""
	for num in array_sort:
		num_str=str(num)
		array_str=array_str+","+num_str
	array_str=array_str+"."
	array_str=array_str[1:]
	# return array_str
	document.getElementById("sorted").innerHTML = array_str

def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value
	# print(value)
	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return
	
	# #value = "        8, 5  , 1,  9,2,  4,1"
	# Your code should start from here
	# store the final string to the variable array_str
	arr = [val.strip() for val in value.split(',')]
	# print(arr)
	arr = [int(el) for el in arr]
	# print(arr)
	array_sort=sort_func(arr)
	array_str = ""
	for num in array_sort:
		num_str=str(num)
		array_str=array_str+","+num_str
	array_str=array_str+"."
	array_str=array_str[1:]
	# print(array_str)

	document.getElementById("sorted").innerHTML = array_str

def sort_func(arr):
	n=len(arr)
	swap=True
	while swap==True:
		swap=False
		new_n=0
		for inner_iter in range(1,n):
			first_num=arr[inner_iter-1]
			second_num=arr[inner_iter]
			if second_num<first_num:
				arr[inner_iter]=first_num
				arr[inner_iter-1]=second_num
				print(arr)
				swap=True
				new_n=inner_iter
		n=new_n
	return arr
# arr=[8, 6, 5, 7, 2, 4, 1, 9, 3, 0]
# print(sort_func(arr))

# print(sortnumber1())
# print(sortnumber2())