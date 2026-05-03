from simple_calculator_class import MoreFeaturesCalculator
def calculator_menu():
    print("")
    print("╔═══════════════════ \033[0;32mRAD CALCULATOR\033[0m ════════════════════╗")
    print("║\033[4mAvailable operations:\033[0m                                  ║")
    print("║  [1] \033[1;33m+\033[0m  -> Addition                                   ║")
    print("║  [2] \033[1;34m-\033[0m  -> Subtraction                                ║")
    print("║  [3] \033[1;32m*\033[0m  -> Multiplication                             ║")
    print("║  [4] \033[1;35m/\033[0m  -> Division                                   ║")
    print("║  [5] \033[1;31m**\033[0m -> Exponent (Power)                           ║")
    print("║  [6] \033[1;36m%\033[0m  -> Modulo (Remainder)                         ║")
    print("║  [7] \033[1;37m%\033[0m  -> Percentage                                 ║")
    print("║  [8] \033[1;36mavg\033[0m -> Average (multiple numbers)                ║")
    print("║                                                       ║")
    print("║ \033[3mDid you know?\033[0m The word \033[0;32mRad\033[0m is a slang for \033[1;31mMAANGAS!!\033[0m   ║")
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

                elif user_choice == "5":
                    calculator.exponential()

                elif user_choice == "6":
                    calculator.remainder()

                elif user_choice == "7":
                    calculator.percent()

            elif user_choice == "8":
                values = input("Enter values(space separated): ")
                separated_values = values.split()

                num_list =[]
                for item in separated_values:
                    num_list.append(float(item))

                calculator.average(num_list)

            else:
                print("Invalid choice. Please try again.")
                continue
        except:
            print("Invalid input. Please try again.")

        retry = input("Do you want to use the RAD CALCULATOR again?(yes/no):")
        if retry != "yes":
            print("Thank you for using RAD CALCULATOR! Turning off...")
            break

if __name__ == "__main__":
    main()




