class Employee:
    name = 'Shakir'
    company = 'OpenAI'
    def show(self):
        print(f'The name of the empoyee is {self.name} and company is {self.company}')

class Coder:
    language = 'Python'
    def showLanguage(self):
        print(f'The coder is a specialist in {self.language}')


class Programmer(Employee, Coder):
    company = 'Anthropic'
    def ProgrammingLanguage(self):
        print(f'The name is {self.name} and he is good in {self.language} language')

a = Employee()
b = Programmer()

a.show()
b.showLanguage()
b.ProgrammingLanguage()