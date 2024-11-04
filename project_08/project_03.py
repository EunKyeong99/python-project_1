class Employee:
    def __init__(self):
        self.name = input("이름 : ")
        self.salary = int(input("급여 : "))

    def display_info(self):
        print("이름 : ", self.name, "/ 급여 : ", self.salary)

information = Employee()
information.display_info()

class Manager:
    def __init__(self):
        self.team_members = []

    def add_team_member(self, employee):
        self.team_members.append(employee)

    def display_team(self):
        return self.team_members

team_information = Manager()
team_information.add_team_member(information.name)

while True:
    user_input = input("추가할 직원 이름 (없을 시 q 입력) : ")
    if user_input.lower() == 'q':
        break
    team_information.add_team_member(user_input)

print("팀원 목록 : ", team_information.display_team())

