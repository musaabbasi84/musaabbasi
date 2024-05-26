'''
Program-5:
Tupes Are unmutable, it means we can not change list elements after creation
'''
#Change the 4th element to 100, it gives error
#Python compiler gives error, the error is TypeError: 'tuple' object does not support item assignment
numbers=(10,20,30,40,50)
print(numbers)
numbers[4]=100
print(numbers)

