class Employee:
    def __init__(self):
        self.name = input("이름 : ")
        self.salary = int(input("급여 : "))

    def display_info(self):
        print("이름 : ", self.name, "/ 급여 : ", self.salary)

class Manager:
    def __init__(self):
        self.team_members = []

    def add_team_member(self):
        employee = input("추가할 직원 이름 : ")
        employee += Employee
        self.team_members.append(employee)

    def display_team(self):
        print(team_information)

information = Employee()
team_information = Manager()

information.display_info()
team_information.display_team()
