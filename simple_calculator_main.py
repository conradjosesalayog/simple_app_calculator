from simple_calculator_class import MoreFeaturesCalculator
def calculator_menu():
    print("")
    print("╔═══════════════════ \033[0;32mRAD CALCULATOR\033[0m ════════════════════╗")
    print("║\033[4mAvailable operations:\033[0m                                  ║")
    print("║  [1] +  -> Addition                                   ║")
    print("║  [2] -  -> Subtraction                                ║")
    print("║  [3] *  -> Multiplication                             ║")
    print("║  [4] /  -> Division                                   ║")
    print("║  [5] ** -> Exponent (Power)                           ║")
    print("║  [6] %  -> Modulo (Remainder)                         ║")
    print("║  [7] %  -> Percentage                                 ║")
    print("║  [8] avg -> Average (multiple numbers)                ║")
    print("║                                                       ║")
    print("║\033[3m Did you know?: The word 'Rad' in tagalog is MAANGAS!!\033[0m ║")
    print("╚═══════════════════════════════════════════════════════╝")

def main():
    calculator = MoreFeaturesCalculator()

    while True:
        calculator_menu()
        user_choice = input("Choose an operation(1-8):")

        try:
            if user_choice in ["1", "2", "3", "4", "5", "6", "7"]:
                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))

                calculator.numbers(first_number, second_number)

                if user_choice == "1":
                    calculator.add()

                elif user_choice == "2":
                    calculator.subtract()

                elif user_choice == "3":
                    calculator.multiply()

                elif user_choice == "4":
                    calculator.divide()

