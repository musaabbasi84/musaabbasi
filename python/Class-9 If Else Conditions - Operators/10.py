print("******************")
print("Welcome To HR App")
print("******************")
print("Enter Option (1-4), 4 is to exit.")
option=int(input("Enter the option: "))
employeeName=input("Enter the employee name: ")
if option == 1:
    # Perform employee performance review
    print("\nPerforming employee performance review...")
    # Add code to evaluate employee performance
    performance_rating = float(input("Enter the employee's performance rating (out of 10): "))
    if performance_rating >= 8:
        print("Excellent performance!")
    elif performance_rating >= 6:
        print("Good performance.")
    else:
        print("Needs improvement.")

elif option == 2:
    # Perform employee training and development
    print("\nPerforming employee training and development...")
    # Add code for training and development activities
    training_program = input("Enter the name of the training program: ")
    print("Enrolling", employeeName, "in", training_program)

elif option == 3:
    # Manage employee leave
    print("\nManaging employee leave...")
    # Add code for leave management system
    leave_type = input("Enter the type of leave (e.g., vacation, sick leave): ")
    leave_duration = int(input("Enter the duration of leave (in days): "))
    print(employeeName, "has been granted", leave_duration, "days of", leave_type, "leave.")

elif option == 4:
    print("\nExiting the HR App...")
    # Add any cleanup or closing code here

else:
    print("\nInvalid option selected. Exiting the HR App...")
