#just like dictonary
#It is the collection of non repetattive numbers
#we can modify list
#unordered , unindexed , unchangeble
b = set()
print(type(b))

#to add values
b.add(4)
b.add(6)
b.add(6)
b.add(5)

#if we add any number repetedly then
#set only store single non repetative value

#we can not add list into set
#because list is mutable
#b.add([1,2,3])
#gives error

#we can add tuples
b.add((1,2,3))
print(b)

#len functions
print(len(b))

#remove function by value
b.remove(6)
print(b)

#pop function
b.pop()
#it removes element from the starting 
print(b)

#clear funtion
b.clear()
#empty the set

#union and intersecton
b.union()
b.intersection()