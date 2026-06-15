from simple_calculator_class import SimpleCalculator

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


