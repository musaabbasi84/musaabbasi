#Find odd number
#Any digit divided by 2 and is not equal to 0 is odd
a=input("Enter a number:")
#Inside input, the number is string we have to convert it into number with int()
a=int(a)
if a%2!=0:
    print("It is odd number")
else:
    print("It is not odd number")
    