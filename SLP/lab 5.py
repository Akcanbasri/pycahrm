from datetime import date

from lab5_model import User


class UserController:
    def __init__(self):
        self.users = []

    def create_user(self, name, last_name, address, gender, birth_date, start_date=date.today()):
        u = User(name, last_name, address, gender, birth_date)
        self.users.append(u)

    def print_users(self):
        for user in self.users:
            print(user)


m = "male"
f = "female"
gender = m or f
add1 = ("85-796", "Kaliskiego st.", 15)
add2 = ("85-796", "Fordonska st.", 21)
add3 = ("85-796", "Jagellon st.", 48)
add4 = ("85-796", "Gdanski st.", 4)
add5 = ("85-796", "Kaliskiego", 16)
user_controller = UserController()
user_controller.create_user("Hasan Basri", "AKCAN", add1, m, date(1999, 2, 4))
user_controller.create_user("Mukaddder", "AKCAN", add2, f, date(1961, 9, 17))
user_controller.create_user("Mustafa", "AKCAN", add3, f, date(1963, 4, 3))
user_controller.create_user("Reyyan", "AKCAN", add4, m, date(2004, 4, 16))
user_controller.create_user("Furkan", "AKCAN", add2, m, date(1983, 4, 16))
user_controller.print_users()