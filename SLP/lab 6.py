from datetime import date

from model import User


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
user_controller.create_user("Bora", "Altuntas", add1, m, date(2000, 2, 4))
user_controller.create_user("Ebru", "Altuntas", add2, f, date(1975, 9, 17))
user_controller.create_user("Ali", "Altuntas", add3, f, date(1966, 4, 3))
user_controller.create_user("Zuhal", "Altuntas", add4, m, date(1996, 4, 16))
user_controller.create_user("Baris", "Altuntas", add2, m, date(2000, 4, 16))
user_controller.print_users()