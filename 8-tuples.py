#tuple is created by using '()' 
#We can not modify the tuples
t =(1,2,3,4)
print(t)

#as we know tuples are immutable.
#following code  show error
#t[0]=0
#print(t)

#empty tuple
t1 = ()
#single value tuple
t2 = (786,)
print(type(t2))
#error format
t3 = (999) #int type
print(type(t3))

t4 = (0,0,2,4,1,1,0,4,0,1,2,3,1,1,2,4,0,0,3)

#count function
print(t4.count(1))
#index finding
print(t4.index(4))

#cannot modify the tuple
#t4.append(0)
#print(t4[-1])