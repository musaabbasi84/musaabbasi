'''
Lamda Function:
Anonymous function to calculate something and return 
'''
def myfunction(a):
    return lambda b:a*b 
mydoubler=myfunction(2)
mytripler=myfunction(3)
print(mydoubler(2))
print(mytripler(4))