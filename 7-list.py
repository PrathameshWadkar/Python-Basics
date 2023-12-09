#Ita an list containing different elements
#just like arrays
a = [ 1 , 5 , 23, 546, 999]
#to print the whole list
print(a)
#Accessing elements with index
print(a[0])
print(a[1])
print(a[2])

#slicing
friends =[ "Prathamesh","abrar","tushar","avinash","rushikesh"]
print(friends[:4])
print(friends[-4:])

#sorting function
l = [23,45,99,23,14,87,51]
print(l)
l.sort()
print(l)
'''
#wrong formats
l1 =l.sort()
print(l1)
print(l.sort())'''

#reversing the list
l.reverse()
print(l)

#appending 
#It adds element at the end of the list
l.append(7)
print(l)

#inserting 
#adding element at the specific index
l.insert(2,36)
print(l)

#poping an element i.e removing using index
l.pop(4)
print(l)

#remove function
#removing element by value
l.remove(36)
print(l)