class SimpleCalculator:
    def __init__(self):
        self.first_number = 0
        self.second_number = 0
        self.result = 0

    def numbers(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def add(self):
        self.result = self.first_number + self.second_number
        print(f"\n Result: {self.result}")

    def subtract(self):
        self.result = self.first_number - self.second_number
        print(f"\n Result: {self.result}")

    def multiply(self):
        self.result = self.first_number * self.second_number
        print(f"\n Result: {self.result}")

    def divide(self):
        if self.second_number == 0:
            print("The first number cannot be divided by zero!")
        else:
            self.result = self.first_number / self.second_number
            print(f"\n Result: {self.result}")

class MoreFeaturesCalculator(SimpleCalculator):
    def exponential(self):
        self.result = self.first_number ** self.second_number
        print(f"\n Result: {self.result}")

    def remainder(self):
        self.result = self.first_number % self.second_number
        print(f"\n Result: {self.result}")

    def percent(self):
        if self.second_number == 0:
            print("Zero cannot be a whole!")
        else:
            self.result = self.first_number / self.second_number * 100
            print(f"\n {self.first_number}% of {self.second_number} is {self.result}%")

    def average(self, number_list):
        if number_list is len(number_list) == 0 or None:
            print("No numbers entered!")
        else:
            total_sum = 0
            for number in number_list:
                total_sum += number
            self.result = total_sum / len(number_list)
            print(f"\n Average: {self.result}")