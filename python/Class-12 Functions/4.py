#Write a function to display your name
#define function first
def displayName(firstName,lastName): #with argument and return value
    fullName=firstName+" "+lastName
    return fullName 
#function will be executed when it is called 
#Call above function with arguments
name=displayName("Ali","Ahmed")
print("My name is ",name)
name=displayName("Hamnah","Ali")
print("My name is ",name)
name=displayName("Yasin","Mohd")
print("My name is ",name)