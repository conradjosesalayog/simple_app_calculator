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
