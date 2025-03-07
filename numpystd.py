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



# ADVANCED NUMPY

#advanced indexing

a=np.arange(24).reshape(6,4)

#fancy indexing

row1 = a[[0,2,3]]
column1 = a[:,[0,2]]

print(f"{row1}\n\n{column1}")


#boolean indexing
b=np.random.randint(1,100,24).reshape(6,4)
print(b)
c = [b >50]

#find numbers greater than 50
d=b[b > 50 ]
print(f"{c}\n\n{d}")

#find out even numbers
e1=b[b%2 == 0]

#find all numbers are greater than 50 and are even
f= b[(b > 50) & (b % 2 == 0)]
print(f)

#find all the number not divisible by 7

g = b[~(b % 7 ==0)]
print(g)




#Broadcasting

a=np.arange(12).reshape(4,3)
b=np.arange(3)
print(a+b)
#braodcasting is done because we add 1 into the head of lower array which is 1D and then extend it.

c=np.arange(3).reshape(1,3)
d=np.arange(4).reshape(4,1)
print(c+d)
#braodcasting is done because there is ones to extend

e2=np.arange(12).reshape(3,4)
f=np.arange(12).reshape(4,3)
print(e1+f)
#braodcasting is not done because there is ones to extend


#Mathematical operation with numpy

#sigmoid

def sigmoid(array):
    return 1 /(1 + np.exp(-array))

a=np.arange(10)
result = sigmoid(a)
print(result)


# mean square error

actualval = np.random.randint(1,100,25)
predictedval = np.random.randint(1,100,25)

def mse(actual,predicted):
    return np.mean((actual - predicted)**2)

result1 = mse(actualval,predictedval)
print(result1)


#binary cross entropy
actual1 = np.array([0, 1, 1, 0, 1])
predicted1 = np.array([0.1, 0.9, 0.8, 0.2, 0.7])

def bce(actual,predicted):
    return -np.mean(actual1 * np.log(predicted1) + (1-actual1) * np.log(1 - predicted1))

result2 = bce(actual1,predicted1)
print(result2)


# Working with missing values

# nan values

a= np.array([1,2,3,4,np.nan,6])
# here we boolean indexing to find missing values
result1 = a[np.isnan(a)]
result2 = a[~(np.isnan(a))]
print(result1)
print(result2)


# Plotting Graphs

import matplotlib.pyplot as plt

#graph of y=x

x= np.linspace(-10,10,100)
y = x
result = plt.plot(x,y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of y=x")
plt.show()


# Graph of y = x**2

x=np.linspace(-10,10,10)
y = x**2

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of y=x")
plt.show()

# Graph of y = sin(x)

x=np.linspace(-10,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of y = sin(x)")
plt.show()


# Graph of y= xlog(x)

x=np.linspace(-10,10,100)
y = x * np.log(x)

plt.plot(x,y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of y = xlog(x)")
plt.show()


# Grap of sigmoid
x=np.linspace(-10,10,100)
y = 1/(1 + np.exp(-x))

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph of y = xlog(x)")
plt.show()


######################### Numpy Functions ##################################

# sort

a= np.random.randint(1,50,15)
b= np.random.randint(1,50,24).reshape(6,4)

result1 = np.sort(a)
result2 = np.sort(b)

result3 = np.sort(a)[::-1]
result4 = np.sort(b ,axis = 0)
print (f"{result1}\n\n{result2}\n\n{result3}\n\n{result4}")


#append

result5 = np.append(a,55)
result6 = np.append(b,np.ones((b.shape[0],1,)),axis = 1)
print(f"{result5}\n\n{result6}")


# concatenate

c= np.arange(6).reshape(2,3)
d= np.arange(6,12).reshape(2,3)

result7 = np.concatenate((c,d),axis = 0)
result8 = np.concatenate((c,d),axis = 1)

print(f"{result7}\n\n{result8}")


#unique

e3= np.array([1,1,2,2,3,4,5,6,6,7])
result9 = np.unique(e3) # get only unique values
print(result9)


#expand_dims

f= np.random.randint(1,50,15)
result10 = np.expand_dims(f, axis =0)
result11 = np.expand_dims(f, axis =1)

print(f"{result10}\n\n{result11}")


#where

g= np.random.randint(1,100,15)
result12 = np.where(g>50)
result13 = np.where(g>50 ,1 ,g)

print(f"{result12}\n\n{result13}")


h = np.random.randint(1,50,15)
i = np.random.randint(1,50,24).reshape(6,4)

result14 = np.argmax(h)
result15 = np.argmax(i , axis =0)
result16 = np.argmax(i , axis =1)

result17 = np.argmin(i , axis =0)
result18 = np.argmin(i , axis =1)

print(f"{h}\n\n{i}\n\n{result14}\n\n{result15}\n\n{result16}\n\n{result17}\n\n{result18}")


#cumsum

j = np.random.randint(1,100,15)
i = np.random.randint(1,50,24).reshape(6,4)
result19 = np.cumsum(j)
result20 = np.cumsum(i)
result21 = np.cumsum(i , axis= 0)
result22 = np.cumsum(i, axis = 1)
result23 = np.cumprod(i)

print(f"{j}\n\n{i}\n\n{result19}\n\n{result20}\n\n{result21}\n\n{result22}\n\n{result23}")


#percentile

k = np.random.randint(1,100,15)
i = np.random.randint(1,50,24).reshape(6,4)
result24= np.percentile(k,100)
result25 = np.percentile(k, 50)
print(result24,result25)


#histogram

l = np.random.randint(1,100,25)
result26 = np.histogram(l,bins= [0,10,20,30,40,50,60,70,80,90,100])
print(result26)

#flip

m = np.array([10,20,30,40,50,60,70,90,100])
n = np.random.randint(1,50,24).reshape(6,4)

result27 = np.flip(m)
result28 = np.flip(n)
print(f"{result27}\n\n{result28}")

#put

o = np.array([10,20,30,40,50,60,70,90,100])
np.put(o, [1, 4], [80, 500])


# delete

p = np.array([10,20,30,40,50,60,70,90,100])
result30 = np.delete(p,[0,1,3])
print(result30)
print(p)


################# Set functions #################


m = np.array([1,2,3,4,5])
n = np.array([3,4,5,6,7])

# union1d

result1= np.union1d(m,n)
print(result1)

#intersect1d
result2 = np.intersect1d(m,n)
print(result2)

#setdiff1d
result3 = np.setdiff1d(m,n)
print(result3)

# setxor1d
result4 = np.setxor1d(m,n)
print(result4)

# isin
result5 = np.isin(m,1)
print(result5)

#clip

arr = np.random.randint(1,100,25)
result6 = (np.clip(arr, 25 ,75))
















