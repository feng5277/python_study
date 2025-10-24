# 类的继承
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_info(self):
        print(self.name,self.id)
class FullTimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,name,id,work_days,daily_salary):
        super().__init__(name,id)
        self.work_days = work_days
        self.daily_salary = daily_salary
    def calculate_salary(self):
        return self.work_days * self.daily_salary

zhangshan = FullTimeEmployee("张三","10054",6000)
lisi = PartTimeEmployee("李四","10059",30,150)
zhangshan.print_info()
print(zhangshan.calculate_salary())
lisi.print_info()
print(lisi.calculate_salary())
