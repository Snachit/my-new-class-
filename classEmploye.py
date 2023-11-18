class Employe :
    def __init__(self, name, baseSalary, bonusHrs, sales) :
        self.name = name
        self.sales = sales
        self.bonusHrs = bonusHrs
        self.baseSalary = baseSalary

    def calculate_net_Salary(self):
        bonus = self.bonusHrs * 10 
        return self.baseSalary + bonus + (self.baseSalary)
    def info(self):
        net_salary = self.calculate_net_Salary()
        print(f"The employee {self.name} hase a base salary of {self.baseSalary} DHS, sales of {self.sales}, and a net salary of {net_salary}")
# Exemple  of usage
emp1 = Employe("Said", 1500, 40, 700)
emp1.info()

        