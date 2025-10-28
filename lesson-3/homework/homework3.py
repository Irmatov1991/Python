#-1-
fruits = ('apple', 'banana', 'cherry', 'orange', 'grapes')
print(fruits[2])

#-2-
list1 = [1,2,3]
list2 = [4,5,6]

combained_list = list1 + list2
print(combained_list)
#-3-

numbers = [10,20,30,40,50,60,70]

first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]   
print(first, middle, last)
#-4-

movies = ['godfather','the matrix', 'xxx','inception','fight club']

movies_tuple = tuple(movies)
print(movies_tuple)
#-5-
cities = ('new york', 'los angeles', 'Paris', 'houston', 'phoenix')

if 'Paris' in cities:
    print("Paris is in the list") 
else:
    print("Paris is not in the list")
#-6-
numbers = [1, 2, 3, 4, 5, 6,]
duplicated_numbers = numbers * 2
print(duplicated_numbers) 
#-7-

numbers = [5, 10, 15, 20, 25]
numbers [0], numbers[-1]=numbers[-1],numbers[0]
print(numbers)
#-8-

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice_tuple = tuple(numbers[3:7])
print(slice_tuple)
#-9-
colors = ['red', 'green', 'blue', 'yellow', 'purple']
#-10
animals = ('cat', 'dog', 'elephant', 'tiger', 'lion')
index_lion = animals.index('lion')
print('the index of lion is', index_lion)
#-11
tuole1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuole1 + tuple2
print(combined_tuple)
#-12
number_list = [10, 20, 30, 40, 50]
nembers_tuple =(1,2,3,4,5)
print('Length of list', len(number_list))
print('Length of tuple', len(nembers_tuple))
#-13
my_tuple = (10,20,30,40,50)
my_list = list(my_tuple)
print('tuple',my_tuple)
print('converted list',my_list)
#-14
numbers = (5,10,8,55,16,78)
max_num = max(numbers)
min_num = min(numbers)

print('maximum_numbers',max_num)
print('minumum_numbers',min_num)
#-15
words = ('apple', 'banana', 'cherry', 'date')
reserved_words = words[::-1]
print('original_tuples', words)
print('reversed_tuples', reserved_words)


