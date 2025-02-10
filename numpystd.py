import numpy as np


#1D array or vector
a = np.array([1,2,3,4])
print(a)
print(type(a))

#2D array or matrices
b= np.array([[1,2,3,4],[4,5,6,7]],dtype=float) # we can define datatype using dtype parameter
print(b)
print(type(b))

#3D array or tenser
c = np.array([[[1,2,3],[4,5,6]],[[3,4,5],[7,3,7]]])
print(c)
print(type(c))

#functions of numpy
#1-- arange

d = np.arange(2,10,2)
print(d)

#2 -- reshape
e= np.arange(1,16).reshape(3,5)
print(e)

#3 ones , zeroes and random

f= np.ones([2,3],dtype=int)
print(f)

g = np.zeros([2,3])
print(g)

h= np.random.random((4,2))
print(h)


#4 np.linspace and np.identity
i= np.linspace(-10,10,10)
print(i)

j= np.identity(3) # diagonal items is 1 and others are zero
print(j)

# ARRAY ATTRIBUTES

a1 = np.array([1,2,3,4])

a2= np.array([[1,2,3,4],[4,5,6,7]])

a3 = np.array([[[1,2,3],[4,5,6]],[[3,4,5],[7,3,7]]])


#ndim
a=a1.ndim
b=a2.ndim
c=a3.ndim

print(f"dimension of the given arrays are \na1={a}\na2={b}\na3={c}")


# shape used to get shape of the array
a=a1.shape
b=a2.shape
c=a3.shape

print(f"shape of the given arrays are \na1={a}\na2={b}\na3={c}")

# size used to get shape of the array
a=a1.size
b=a2.size
c=a3.size

print(f"size of the given arrays are \na1={a}\na2={b}\na3={c}")

# size used to get shape of the array
a=a1.itemsize
b=a2.itemsize
c=a3.itemsize

print(f"itemize of the given arrays are \na1={a}\na2={b}\na3={c}")

# size used to get shape of the array
a=a1.dtype
b=a2.dtype
c=a3.dtype

print(f"datatype of the given arrays are \na1={a}\na2={b}\na3={c}")


#changing datatype

a=a1.astype(np.int32)
print(a.dtype)

#ARRAY OPERATIONS

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12).reshape(3,4)
print(f"{a1}\n{a2}\n")

#SCALAR OPERATIONS
#arthematic operations with a single number

result1 = a1*2
result2 = a2*2
result3 = a1+2
result4 = a2/2

print(f"{result1}\n{result2}\n{result3}\n{result4}")


result5=a2>5
print(result5)

result6 = a1>=7
print(result6)


# VECTOR OPERATIONS

results7 = a1 + a2
results8 = a1 * a2
print(results7)
print(results8)

'''

'''
#ARRAY FUNCTION
# max/min/sum/prod

a1 = np.random.random((3,3))
a1 = np.round(a1*100)

b=np.max(a1)
c=np.min(a1)
d=np.sum(a1)
e=np.prod(a1)

print(f"{b}\n{c}\n{d}\n{e}")

# axis = 0 is column and axis 1 = row
f1 = np.max(a1, axis = 1) #gives max in row
f2 = np.max(a1, axis = 0)#give max in column
g1 = np.min(a1, axis = 1)# give min in row
g2 = np.min(a1, axis = 0)# give min in column

print (a1)
print(f"\nmax in row{f1}\nmax in column{f2}\nmin in row{g1}\nmin in column{g2}")



#mean/median/std/var

me = np.mean(a1)
md= np.median(a1)
st= np.std(a1)
v=np.var(a1)

print(f"\nmean is {me}\nmedian is {md}\nstandard deviation is {st}\nvariance is {v}")


#Dot Product

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(4,3)

print(f"{a1}\n{a2}\n")
result1 = np.dot(a1,a2)
print (result1)

# log and exponent

result2 = np.log(a1)
result3 = np.exp(a1)
print(f"\n{result2}\n{result3}")

'''

'''
#round/floor/ceil

result4 = np.round(np.random.random((2,3))*100).astype(int)

result5 = np.floor(np.random.random((2,3))*100).astype(int)

result6 = np.ceil(np.random.random((2,3))*100).astype(int)

print(f"{result4}\n\n{result5}\n\n{result6}")


# Indexing and slicing

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(27).reshape(3,3,3)

'''
a1=[0 1 2 3 4 5 6 7 8 9]  

a2=[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]

a3=[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]]

 [[ 9 10 11]
  [12 13 14]
  [15 16 17]]

 [[18 19 20]
  [21 22 23]
  [24 25 26]]]
'''

print(f"{a1}\n\n{a2}\n\n{a3}")

# Indexing
b= a1[-1:-4]
print(b)

c=a2[:2,1:]
print(c)

d=a3[::2,0,::2]
print(d)



#Iterating

for i in a1:
    print(i)

for i in a2:
    print(i)

for i in a3:
    print(i)


# nditer function

for i in np.nditer(a2):
    print(i)

for i in np.nditer(a3):
    print(i)

print(a2)

c=np.transpose(a2)
d = a2.T
print(c)
print(d)

#ravel -- convert the any dimensional array into 1D

# e= a2.ravel()
# print(e)


#stacking  -- joint two array

a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
print(f"{a4}\n\n{a5}")

# two type stacking

#  a- horizontal stacking
#  [3,4] ,[3,4]  = [3,8]

a=np.hstack((a4,a5))
print(a)

# b- vertical stacking
#  [3,4] , [3,4] = [6,4]

b=np.vstack((a4,a5))
print(b)


#spliting

c = np.hsplit(a4,2)
print(c)
d = np.vsplit(a4,3)
print(d)


# array vs list speed
import time
a = [i for i in range(10000000)]
b= [i for i in range (10000000,20000000)]

c= []

start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])
print(time.time() - start)

c = np.arange(10000000)
d = np.arange(10000000,20000000)
start = time.time()
e= c +d
print(time.time() - start)



# array vs list memory size

import sys

f = [i for i in range(10000000)]
size1=sys.getsizeof(f)
print(size1)

g = np.arange(10000000,dtype=np.int8)
size2=sys.getsizeof(g)
print(size2)



















