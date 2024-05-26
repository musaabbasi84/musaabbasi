# Define department names
departments = ("Sales", "Marketing", "Finance", "HR", "Operations")

# Initialize empty lists for each department's data
department_data = ([], [], [], [], [])

# Collect data from the user for each department
for i, department in enumerate(departments):
    print(f"Enter data for {department} department:")
    for j in range(5):
        data_point = input(f"Enter data point {j + 1} for {department}: ")
        department_data[i].append(data_point)

# Display reports for each department
print("\nReports for the departments:")
for department, data in zip(departments, department_data):
    print(f"{department} department report:")
    for i, data_point in enumerate(data, start=1):
        print(f"{i}. {data_point}")
    print()
