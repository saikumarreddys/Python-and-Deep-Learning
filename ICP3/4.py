
class Employee():


    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department


    def AvgSalary(self,Emplist):
        count=0
        TotalSalary=0
        for i in Emplist:
            count = count+1
            TotalSalary = TotalSalary + i.salary



        avg = (TotalSalary) /count;

        print("The Average Salary is {}".format(avg))
    def Display(self,Emplist):

        print("--- Employee Details are ----- ")
        for i in Emplist:
            print(i.name, i.family, i.salary, i.department)



class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)





def main():
    EmployeeList = [];

    choice = input(" Do you want to add an employee :")

    while(choice=='yes'):
        name = input(" Enter the name of the employee :")
        family = input(" Enter family name :")
        salary = int(input(" Enter the salary :"))
        department = input(" Enter the department :")
        e1 = Employee(name,family,salary,department)
        EmployeeList.append(e1);
        choice = input(" Do you want to add an employee :")

    e1.AvgSalary(EmployeeList)
    f1=FullTimeEmployee(EmployeeList)
    f1.Display(EmployeeList)




if __name__=="__main__":
    main()
