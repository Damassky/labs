class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_pass(self, new_pass):
        self.password = new_pass

    def check_pass(self, password):
        return self.password == password


user = UserAccount("customer", "email", "1357")
user.set_pass("1234")
print(user.check_pass("4321"))
print(user.check_pass("1234"))


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"manufacturer: {self.make}, model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, fuel type: {self.fuel_type}"


car = Car("McLaren", "765LT", "petrol")
print(car.get_info())