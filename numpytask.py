import numpy as np

'''
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

'''

'''Q-7: Consider a random integer (in range 1 to 100) vector with shape (10,2) representing coordinates, and coordinates 
of a point as array is given. Create an array of distance of each point in the random vectros from the given point. 
Distance array should be interger type.


cords = np.random.randint(1,100,size=(10,2))
given_point = np.array([2,3])

distance = np.linalg.norm(cords - given_point , axis=1)
distances = distance.astype(int)

print(distances)

'''

'''Q-8: Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?

arr=np.zeros((6,7,8))
print(arr)
result = np.unravel_index(100,(6,7,8))
print(result)
'''

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


input_numbers =input("Enter the numbers: ")
arr = np.array(input_numbers.split(), dtype =float)
reversed_arr = arr[::-1]

print(reversed_arr)




Q-10: Elements count
Count the number of elements of a numpy array.


num_element = input("Enter the element of array: ")
arr = np.array(num_element.split())
count_element = arr.size
print (count_element)
print(arr)



Q-11: Softmax function
Create a Python function to calculate the Softmax of the given numpy 1D array. The function only accepts the numpy 1D array, otherwise raise error.


def softmax(arr):
    if type(arr) != np.ndarray:
        raise TypeError ("requires a numpy array")
    elif arr.ndim > 1:
        raise TypeError("requires 1D array")
    total=np.sum(np.exp(arr))
    return np.exp(arr)/total

arr_input = input("Enter the your array: ")
arr = np.array(arr_input.split(),dtype=float)

result = softmax(arr)
print(result)
'''

'''Q-12: Vertical stack
Write a python function that accepts infinite number of numpy arrays and do the vertical stack to them. Then return that new array as result.
The function only accepts the numpy array, otherwise raise error.


def ver_stack(*args):
    if args != np.ndarray:
        raise TypeError("requires an array")
    return np.vstack(args)

a = np.arange(10).reshape(2,5)
print("a=",a)
b = np.arange(1,11).reshape(2,5)
print("b=",b)

result = ver_stack((a,b))
print (result)
'''


'''  Q-13: Dates
Create a python function named date_array that accepts two dates as string format and returns a numpy array of dates between those 2 dates. 
The function only accept 2 strings, otherwise raise error. The date format should be like this only: 2022-12-6. 
The end date should be included and for simplicity, choose dates from a same year.


def date_array(date1: str,date2: str):
    if type(date1) != str or type(date2) != str:
        raise TypeError
    try:
        start_date = np.datetime64(date1,'D')
        end_date = np.datetime64(date2, 'D')
    except Exception:
        raise ValueError("The date must be in YYYY-MM-DD format")

    return np.arange(start_date,end_date + np.timedelta64(1, 'D'),dtype="datetime64[D]")

date1=input("Enter your first date: ")
date2=input("Enter your second date: ")

result = date_array(date1,date2)
print(result)
'''

'''
Q-14: Subtract the mean of each row from a matrix.

arr = np.round(np.random.random((5,4))*100)
arr_mean = arr.mean(axis = 1,keepdims=True)
result = arr - arr_mean
print(result)

'''

'''Q-15: Swap column-1 of array with column-2 in the array.

arr = np.arange(9).reshape(3,3)
print(arr)
result = arr[:, [0,2,1]]
print(result)
'''


'''
Q-16: Replace odd elements in arrays with -1.

arr = np.arange(10)
result=np.where(arr%2 ==1 ,-1 ,arr)
print(result)
'''


'''Q-17: Given two arrays of same shape make an array of max out of two arrays. (Numpy way)

a=np.array([6,3,1,5,8])
b=np.array([3,2,1,7,2])
a[b>a] = b[a<b]
print(a)
'''


'''Q-18 Answer below asked questions on given array:
Fetch Every alternate column of the array
Normalise the given array
There are different form of normalisation for this question use below formula.

Xnormalized=X−Xmin/Xmax−Xmin 

arr1=np.random.randint(low=1, high=10000, size=40).reshape(8,5)

arr1=np.random.randint(low=1, high=10000, size=40).reshape(8,5)

result1 = arr1[:,::2]

result2 = (arr1 - arr1.min()) /(arr1.max() - arr1.min())

print(arr1)
print(result1)
print(result2)
'''


'''Q-19: Write a function which will accept 2 arguments.
First: A 1D numpy array arr
Second: An integer n {Please make sure n<=len(arr)}
Output: The output should be the nth largest item out of the array



def nthmax(arr,n):
    if n>len(arr):
        raise IndexError("n is way out of limit")
    arr.sort()
    return arr[-n]

result = nthmax(np.array([ 705,314,5991,5269,4081]),3)
print(result)
'''

'''Q-20: Create the following pattern without hardcoding. Use only numpy functions and the below input array

# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

arr = np.array([1,2,3])
repeat_arr = np.repeat(arr,3)
tile_arr = np.tile(arr,3)
print(repeat_arr)
print(tile_arr)

result = np.hstack((repeat_arr,tile_arr))
print(result)

'''

