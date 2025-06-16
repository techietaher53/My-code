class Employee:
    company = 'OpenAI'
    def show(self):
        print(f'The name of the empoyee is {self.name} and salary is {self.salary}')

class Programmer(Employee):
    company = 'Anthropic'
    def ProgrammingLanguage(self):
        print(f'The name is {self.name} and he is good in {self.language} language')

a = Employee()
b = Programmer()
print(a.company, b.ProgrammingLanguage)