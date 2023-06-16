# Доработайте класс Employee таким образом, чтобы значение переменной self.on_vacation
# принималось извне, как и переменные self.name, self.salary.
# Добавьте новый атрибут, self.is_good_employee, который может принимать значения True или False.
# Сделайте так, чтобы это значение можно было передать в конструктор класса в качестве параметра
# (как в предыдущем задании). Создайте список из пяти сотрудников (класс Employee), где параметр is_good_employee
# – у четверых будет True, а у одного False.
# После этого пройдитесь циклом по всему списку и увольте плохого работника,
# у которого значение self.is_good_employee = False.
#




class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.Good_employee = is_good_employee


Emp1 = Employee(name='Алексей', salary= 12500, on_vacation=False, is_good_employee=True)
Emp2 = Employee(name='Дима', salary= 20500, on_vacation=False, is_good_employee=True )
Emp3 = Employee(name='Николай', salary= 25000, on_vacation=False, is_good_employee=True)
Emp4 = Employee(name='Денис', salary= 50000, on_vacation=False, is_good_employee=True)
Emp5 = Employee(name='Артём', salary= 65000, on_vacation=False, is_good_employee=False)
employee_list  = [Emp1, Emp2, Emp3, Emp4, Emp5]
for employee in employee_list:
    if employee.Good_employee == False:
        print(f'{employee.name} был  уволен, так как он плохой работник')