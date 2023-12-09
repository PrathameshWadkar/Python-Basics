#funtion with return 
def percent(mark):
    return((mark[0]+mark[1]+mark[2]+mark[3])/4)

mark1 =[ 45,67,96,81]
percentage1 =percent(mark1)

marks2 =[ 57,72,63,93]
percentage2 = percent(marks2)

print(percentage1 , percentage2)

#funtion without return
def greet(name):
    print("hello "+name)

greet("harry ")

#funtion with no argument
def greet(name="Stranger"):
#stranger stands for default argument
    print(f" Hello {name}")

greet()

#recursive funtion
