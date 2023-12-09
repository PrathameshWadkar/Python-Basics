#while loop
i=0
while i<10:
    print(i)
    i+=1
k=0
frt = ['banana','apple','mango','grapes']
while k<len(frt):
    print(frt[k])
    k+=1
    
#for loop
for item in frt:
    print(item)

#Range funtion
for z in range (9):
    print(z)

print("\n")

#first digit is starting and next digit is ending
for z in range (5,9):
    print(z)
print("\n")

#the thied parameter is stepsize
#by default it is 1
for z in range (1,9,2):
    print(z)

#else with for loop
#it runs after complete execution of loop
for z in range (9):
    print(z)
else:
    print("naturally executed from loop")

#break in loop
#it abnormally terminates loop
for z in range (9):
    print(z)
    if(z==5):
        break
else:
    print("naturally executed from loop")

#pass with for loop
for z in range (9):
    if(z==5): 
        pass #it jumps to next iteration of loop
    print(z)

