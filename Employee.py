class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def set_name(self, name):
        self.name = name

    def set_id_number(self, id_number):
        self.id_number = id_number

    def set_department(self, department):
        self.department = department

    def set_job_title(self, job_title):
        self.job_title = job_title

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number

    def get_department(self):
        return self.department

    def get_job_title(self):
        return self.job_title

    def __str__(self):
        return ("Name: " + str(self.name) +
                "\nID Number: " + str(self.id_number) +
                "\nDepartment: " + str(self.department) +
                "\nJob Title: " + str(self.job_title))


employeesDictionary = {}


def lookup(id):
    for i in employeesDictionary.keys():
        if i == id:
            print(employeesDictionary[id])
        else:
            print("Employee not found")


def addEmployee():
    emp_id = input("Enter Employee ID Number: ")
    emp_name = input("Enter Employee Name: ")
    emp_department = input("Enter department: ")
    emp_job_title = input("Enter Employee Job Title")

    employee = Employee(emp_name, emp_id, emp_department, emp_job_title)

    key = employee.get_id_number()
    values = [employee.get_name(), employee.get_department(), employee.get_job_title()]
    employeesDictionary[key] = values
    print("Employee Added Successfully")


def updateEmployee(id):
    for i in employeesDictionary.keys():
        if i == id:
            emp_name = input("Enter Employee Name: ")
            emp_department = input("Enter department: ")
            emp_job_title = input("Enter Employee Job Title")
        else:
            print("Employee does not exist")
    employee = Employee(emp_name, id, emp_department, emp_job_title)
    values = [employee.get_name(), employee.get_department(), employee.get_job_title()]
    employeesDictionary[id] = values
    print("Employee Updated Successfully")


def deleteEmployee(id):
    for i in employeesDictionary.keys():
        if i == id:
            print("You have deleted {}".format(str(employeesDictionary.pop(id))))
        else:
            print("The Employee does not exist")


def pickleFile(dictionary):
    save_to_file = open("employees.txt", 'a')
    save_to_file.write(dictionary)



while True:
    print("\n")
    print("Choose 1 to lookup an employee in the dictionary")
    print("Choose 2 to add a new employee")
    print("Choose 3 to update an existing employee")
    print("Choose 4 to delete an employee")
    print("Choose 5 to Quit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            employee_id = input("Enter the employee's ID Number: ")
            lookup(employee_id)

        elif choice == 2:
            addEmployee()

        elif choice == 3:
            employee_id = input("Enter the employee's ID Number: ")
            updateEmployee(employee_id)

        elif choice == 4:
            employee_id = input("Enter the employee's ID Number: ")
            deleteEmployee(employee_id)

        elif choice == 5:
            pickleFile(employeesDictionary.values())
            break

    except:
        print("Wrong input, please enter a value")
