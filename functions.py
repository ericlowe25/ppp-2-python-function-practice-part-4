# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(l,m,n):
    return max(l,m,n)

print(max_num(3,2,4))
print(max_num(3,1,3))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

print(mult_list([4,3,2,1]))
print(mult_list([5,6,7,8]))

# Write a Python function called rev_string() to reverse a string.

def rev_string(myString):
    return myString[::-1]

print(rev_string('Wolfpack Football'))
print(rev_string('Football is fun'))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(z,l,m):
    return z in range(l,m+1)

print(num_within(3,2,4)) #True
print(num_within(3,1,3)) #True
print(num_within(10,2,5)) #False

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1
pascal(2)
pascal(4)






