#include <iostream>
using namespace std;

int main() {
    string employeeName;
    int employeeAge;
    double employeeSalary;

    // Input employee details
    cout << "Welcome to the HR App!" << endl;
    cout << "Please enter the employee's name: ";
    getline(cin, employeeName);
    cout << "Please enter the employee's age: ";
    cin >> employeeAge;
    cout << "Please enter the employee's salary: $";
    cin >> employeeSalary;

    // Perform salary appraisal based on age
    if (employeeAge <= 30) {
        employeeSalary += employeeSalary * 0.05; // 5% increase
    } else {
        employeeSalary += employeeSalary * 0.03; // 3% increase
    }

    // Display employee details with updated salary
    cout << endl;
    cout << "Employee Details:" << endl;
    cout << "Name: " << employeeName << endl;
    cout << "Age: " << employeeAge << endl;
    cout << "Salary: $" << employeeSalary << endl;

    // HR Options
    cout << endl;
    cout << "HR Options:" << endl;
    cout << "1. Employee Performance Review" << endl;
    cout << "2. Employee Training and Development" << endl;
    cout << "3. Employee Leave Management" << endl;
    cout << "4. Exit" << endl;

    int option;
    cout << endl;
    cout << "Enter the option number: ";
    cin >> option;

    if (option == 1) {
        // Perform employee performance review
        cout << endl;
        cout << "Performing employee performance review..." << endl;
        // Add code to evaluate employee performance
        double performanceRating;
        cout << "Enter the employee's performance rating (out of 10): ";
        cin >> performanceRating;

        if (performanceRating >= 8) {
            cout << "Excellent performance!" << endl;
        } else if (performanceRating >= 6) {
            cout << "Good performance." << endl;
        } else {
            cout << "Needs improvement." << endl;
        }

    } else if (option == 2) {
        // Perform employee training and development
        cout << endl;
        cout << "Performing employee training and development..." << endl;
        // Add code for training and development activities
        string trainingProgram;
        cout << "Enter the name of the training program: ";
        cin.ignore();
        getline(cin, trainingProgram);
        cout << "Enrolling " << employeeName << " in " << trainingProgram << endl;

    } else if (option == 3) {
        // Manage employee leave
        cout << endl;
        cout << "Managing employee leave..." << endl;
        // Add code for leave management system
        string leaveType;
        int leaveDuration;
        cout << "Enter the type of leave (e.g., vacation, sick leave): ";
        cin.ignore();
        getline(cin, leaveType);
        cout << "Enter the duration of leave (in days): ";
        cin >> leaveDuration;
        cout << employeeName << " has been granted " << leaveDuration << " days of " << leaveType << " leave." << endl;

    } else if (option == 4) {
        cout << endl;
        cout << "Exiting the HR App..." << endl;
        // Add any cleanup or closing code here

    } else {
        cout << endl;
        cout << "Invalid option selected. Exiting the HR App..." << endl;
    }

    return 0;
}
