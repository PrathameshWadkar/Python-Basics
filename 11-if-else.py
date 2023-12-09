a=5
if a>6:
    print(a)
else:
    print("less than 6")

if(a>10):
    print("greater than 10")
elif(a==5):
    print("same")
else:
    print("less than 5")

#we can use 'is' keyword instead of '=='
if(a is 5):
    print("is keyword")

#we can use empty block by using "pass" keyword
if(a is 5):
    pass

# OR keyword
x= 40
y=36
z=32

if x<35 or y<35 or z<35:
    print("fail")

# IN keyword
text = " this is the fastest way to making money by working from home "

if "fastest way" in text:
    spam = True
elif "making money" in text:
    spam =True
else:
    spam = False

if(spam):
    print("this is working right")
else:
    print("please check the code")