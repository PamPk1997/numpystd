import numpy as np
from fontTools.misc.cython import returns
from numpy.ma.core import arange

# Q-1 Create a null vector of size 10 but the fifth value which is 1.

arr = np.zeros(10)
arr[4] = 1
print (arr)


# Q-2 Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.

a = int(input("Enter your number: "))
b = int(input("Enter your second number: "))

random_arr = np.round(np.random.random((a,b))*100)
print(f"this is the random array {random_arr}")

avg_random_arr = np.mean(random_arr)
print(f"Avg of the random array {avg_random_arr} ")


# Q-3Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.


def create_array(a,b):

    arr = np.zeros((a,b) ,dtype=int)

    arr[0,:]  = 1
    arr[-1,:] = 1
    arr[:,0]  = 1
    arr[:,-1] = 1

    return arr

a = int(input("Enter number: "))
b = int(input("Enter numer: "))

result = create_array(a,b)
print(result)



# Q-4 Create a vector of size 10 with values ranging from 0 to 1, both excluded.

arr = np.random.random(10)
print(arr)

# another

arr = np.linspace(0.1 ,0.9,10)
print(arr)



# Q-5 Can you create a identity mattrix of shape (3,4). If yes write code for it.

ident_arr = np.identity(3).reshape(3,4)
print(ident_arr)
#identity matrix always create elements in it's multiple
# No, cannot reshape array of size 9 into shape (4,3)


# Q-6: Create a 5x5 matrix with row values ranging from 0 to 4.

arr = np.arange(5).reshape(1,-1)
result = np.repeat(arr,5,axis=0)
print(result)



'''Q-7: Consider a random integer (in range 1 to 100) vector with shape (10,2) representing coordinates, and coordinates 
of a point as array is given. Create an array of distance of each point in the random vectros from the given point. 
Distance array should be interger type.'''


cords = np.random.randint(1,100,size=(10,2))
given_point = np.array([2,3])

distance = np.linalg.norm(cords - given_point , axis=1)
distances = distance.astype(int)

print(distances)


'''
Q-9: Arrays
You are given a space separated list of numbers. Your task is to print a reversed NumPy array with the element type float.
Input Format:
A single line of input containing space separated numbers.
Output Format:
Print the reverse NumPy array with type float.
Example 1:
Input:
1 2 3 4 -8 -10
Output:
[-10.  -8.   4.   3.   2.   1.]
'''

input_numbers =input("Enter the numbers: ")
arr = np.array(input_numbers.split(), dtype =float)
reversed_arr = arr[::-1]

print(reversed_arr)



'''
Q-10: Elements count
Count the number of elements of a numpy array.
'''

num_element = input("Enter the element of array: ")
arr = np.array(num_element)
count_element = arr.size
print (count_element)
print(arr)















