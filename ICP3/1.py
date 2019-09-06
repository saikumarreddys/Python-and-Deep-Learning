class Employee():
    count = 0
    TotalSalary = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count = Employee.count + 1
        Employee.TotalSalary = Employee.TotalSalary + self.salary

    def AvgSalary(self):
        avg = (Employee.TotalSalary) / Employee.count;
        print(Employee.TotalSalary)
        print("The Average Salary is {}".format(avg))


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

    def EmpCount(self):
        print(Employee.count)


def main():
    e1 = Employee('Saikumar', 'reddy', 40, 'Manager')
    e2 = Employee('Ram', 'reddy', 40, 'Developer')
    f1 = FullTimeEmployee('sai', 'reddy', 20, 'Architect')
    f1.AvgSalary()


if __name__=="__main__":
    main()
