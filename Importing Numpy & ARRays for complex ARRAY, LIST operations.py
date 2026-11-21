import array as arr
import numpy as np


'''
ARRAY is a collection of elements stored at contiguous memory locations, used to hold multiple values of the same data type.
Unlike LISTS, which can store mixed types, arrays are homogeneous.

They require a typecode during initialization to define the data type:
They are:

"i" for SIGNED INT, SIZE = 4
"f" for FLOAT, SIZE = 4
"b" for CHAR, , SIZE = 1
"YOU DON'T HAVE TO WORRY ABT THIS , THIS IS JUST A INFO, for now"

'''


#SIMPLE LIST OP's
'''
a = [1,2,["a","b"],[3,[3.142,33333]]]
print(a)
print(a[3])
print(a[3][1])
print(a[3][1][0])
'''


#NUMPY LISTS "element wise Op's"
'''
a = [1,2,3,4]   #OR you can also write " a = np.array([1,2,3,4]) and print(a * 2) "
aa = np.array(a)*2   #look next code for clear declaration of the code
print(aa)
'''


#NUMPY LISTS "Multi-Dimensional wise Op's"
'''
a = np.array([[1,2,3],[4,5,6]])
print(a*2)
'''


#ARRAY creation
'''
a = arr.array('i',[9,8,7,6,5])
print(*a)

"OR"

for i in range(0,len(a)):   #no need to write 'len(a)+1' here cuz it just works that way, don't ask too many Q's urself
    print(a[i], end = ' ')
'''


#ARRAY SLLICING
'''
a = arr.array('i', [1,2,3,4,5,6,7,8,9])
print("a[:]   :",a[:]) #PRINTS from beggining
print("a[:7]   :",a[:7]) #PRINTS till 7
print("a[7:]   :",a[7:]) #PRINTS from 7
print("a[3:8] :",a[3:8])
print("a[:-5] :",a[:-5])   #prints from "-5" leaving last ele
print("a[::-1]:",a[::-1])  #prints list in reverse
'''


#ARRAY BASIC OP's using ARR
'''
a = arr.array('i',[1,2,3,4])
print(a[0])
a.append(5) #not '[]' use '()' and also as you know APPEND to add 1 element and EXTEND to add multiple
print(*a)
a.insert(3,7)   #this means inserting 7 at a[3]
print(*a)
'''


#ARRAY BASIC OP's using ARR
'''
a = arr.array('i',[1,2,3,4])
a.remove(1) #removes first occurence of " 1 "
print(*a)
a.remove(4)
print(*a)    #[2,3]

a.insert(0,1)
print(a) #o/p: [1,2,3]
a.pop(1)    #removes the value at index '1'
print(a)    #o/p: [1,3]
'''


#Searching Element
'''
import array
a = array.array('i',[1,2,3,4,5])
print(a.index(5))
'''


#Some other operations
'''
a = arr.array('i',[1,2,2,3,4,2,2,2])    #count of a num in the list 
print("There are",a.count(2), "2's in the list")
'''


#reversing list
'''
a = [1,2,3,4,5]
a.reverse()
print(*a)
'''


#EXTENDING LIST
'''
a = arr.array('i',[1,2,3,4,5])
a.extend([6,7,8,9])
print(*a)
'''    




























