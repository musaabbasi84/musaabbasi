#Password Checker Script
user="ali"
password="abc"
user1=input("Enter admin user:")
password1=input("Enter admin password:")
if user==user1 and password==password1:
    print("Welcome to your profile."+user1)
    print("Email:ali@gmail.com")
    print("Phaone:12345")
    print("Number Of Friends:20")
else:
    print("Sorry! Your credentials are not correct.")
