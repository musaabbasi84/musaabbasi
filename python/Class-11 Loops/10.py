salary=int(input("Enter salary:"))
increment=0
if(salary>10000):
    increment=salary*0.01
else:
    increment=salary*0.05
print("Increment is:",increment)
