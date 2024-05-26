#make calculator function 
def calculator(num1,num2):
    addition=add(num1,num2)
    return addition 
def add(a,b):
    return a+b
 
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
result=calculator(n1,n2)
print("Result is ",result)