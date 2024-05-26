#invoice
name=input("Enter Product Name:")
price=input("Enter Product Price:")
qty=input("Enter Product Qty:")
total=int(price)*int(qty)
print("=======")
print("INVOICE")
print("=======") 
print("Product Name:"+name)
print("Product Price:"+str(price))#convert price to string with str to join +
print("Product Qty:"+str(qty))
print("Total:"+str(total))
