from simple_calculator_class import SimpleCalculator

class MoreFeaturesCalculator(SimpleCalculator):
    def exponential(self):
        self.result = self.first_number ** self.second_number
        print(f"\n Result: {self.result}")

    def remainder(self):
        self.result = self.first_number % self.second_number
        print(f"\n Result: {self.result}")
