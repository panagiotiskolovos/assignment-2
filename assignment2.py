# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(set(numbers))  # set() removes duplicates, sorted() sorts the list
# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
   cum_sum = []
   # initliaze total to 0
   total = 0
   # loop through each number in array
   for num in arr:
       # add number to total
       total += num
       # append total to cum_list
       cum_sum.append(total)
   return cum_sum
    

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    # using splicing, return every Nth element
    return lst[step-1::step]


# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    # be sure lists are same length
    if len(list1) != len(list2):
        print("Lists must be of same length")
    # find dot prodcut
    total = 0 
    for i in range(len(list1)):
        total += list1[i] * list2[i]
    return total


# Test question 1 
print("Question 1:")
# input values
list_numbers = input("Enter a list of numbers separated by sapces: ")
# split string into parts and convert to integers
numbers = [int(num) for num in list_numbers.split()]
# call function
remove_duplicates_and_sort(numbers)
# print result
print("Sorted list with duplicates removed:", remove_duplicates_and_sort(numbers))

# Test question 2
print("Question 2:")
# input values
list_numbers= input("Enter a list of numbers separated by spaces: ")
# split input into parts and convert to integers
arr = [int(num) for num in list_numbers.split()]

# call function
cumulative_sum(arr)

# output result
print("Cumulative sum list:", cumulative_sum(arr))

# Test question 3
print("Question 3:")
# input values
# ask for step value
step = int(input("Enter a step value (N): "))
# ask for list of elements
list_elements = input("Enter a list of elements separated by spaces: ")
# split input into parts
lst = [int(num) for num in list_elements.split()]

# call function
slice_every_nth(lst, step)

# output result
print("Every", step, "th element:", slice_every_nth(lst, step))

# Test question 4
print("Question 4:")
# input values
# ask fpr first list of numbers
input_list1 = input("Enter the first list of numbers separated by spaces: ")
# split first list intp parts and convert to integers
list1 = [int(num) for num in input_list1.split()]
# ask for second list of numbers
input_list2 = input("Enter the second list of numbers separated by spaces: ")
# split second list into parts and convert to integers
list2 = [int(num) for num in input_list2.split()]

# call function
dot_product(list1, list2)

# output results
print("Dot product is", dot_product(list1, list2))


# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
   # determine number of rows and columns for each matrix
   matrix1_rows = len(matrix1)
   matrix1_cols = len(matrix1[0])
   matrix2_rows = len(matrix2)
   matrix2_cols = len(matrix2[0])

   # check if columns in matrix 1 is equal to rows in matrix 2
   if matrix1_cols != matrix2_rows:
       raise ValueError ("The number of columns in matrix 1 must equal to the number of rows in matrix 2")
   
   # create a result matrix filled with zeros
   result = [[0 for _ in range(matrix2_cols)] for _ in range(matrix1_rows)]

   # multiply the matrices
   # for each row in matrix1
   for i in range(matrix1_rows):
       # for each column in matrix 2
       for j in range(matrix2_cols):
           for k in range(matrix1_cols): # shared dimension
               result[i][j] += matrix1[i][k] * matrix2[k][j] # multiply corresponding elemnts and sum them
   return result
# input values
print("Question 5:")
# input values for size of first matrix
matrix1_rows = int(input("Enter the number of rows for Matrix 1:"))
matrix1_cols = int(input("Enter the number of colmns for matrix 1:")) 
print("Enter the elements of Matrix 1 row by row (separate by spaces:")

# create first matrix with input
matrix1 = []
for i in range(matrix1_rows):
    row = list(map(float, input(f"Row{i+1}: ").split()))
    while len(row) != matrix1_cols: # make sure number of elements is correct
        print("Incorrect number of elements")
        row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix1.append(row) # builds matrix

# input values for second matrix
matrix2_rows = int(input("Enter the number of rows for Matrix 2:"))
matrix2_cols = int(input("Enter the number of columns for Matrix 2:"))
print("Enter elements of Matrix 2 row by row (separated by spaces:)")

# create second matrix with input
matrix2= []
for i in range (matrix2_rows):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    while len(row) != matrix2_cols:
        print("Incorrect number of elements")
        row = list(map(float, input(f"Row {i+1}: ").split()))
    matrix2.append(row)

# multiply and output result
product = matrix_multiplication(matrix1, matrix2)
print("\nResult of Matrix Multiplication:")
for row in product:
    print(row)


print("All questions have been completed")