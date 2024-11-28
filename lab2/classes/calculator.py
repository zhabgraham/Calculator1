from shared import app_settings, operations, calc_input_handler, history


class Calculator:
    def __init__(self):
        self.memory = None
        self.history = []

    def calculate(self):
        while True:
            operator = calc_input_handler.get_operator()
            first_operand = calc_input_handler.get_operand("Enter the first operand or MR (Memory recall): ")

            if operator == 'sqrt':
                second_operand = None
            else:
                second_operand = calc_input_handler.get_operand("Enter the second operand or MR (Memory recall): ")

            try:
                result = operations.perform_operation(operator, first_operand, second_operand)
                rounded_result = round(result, app_settings.decimal_places)
                print(f"Result: {rounded_result}")
                history.add_to_history(f"{first_operand} {operator} {second_operand or ''} = {rounded_result}")

                calc_input_handler.perform_memory_operation(rounded_result)
                calc_input_handler.perform_history_operation()
            except Exception as e:
                print(f"Error: {e}")

            repeat = input("Do you want to perform another calculation? (y/n): ").strip().lower()
            if repeat != 'y':
                break

    def run(self):
        while True:
            print("\nMain Menu")
            print("1. Calculator")
            print("2. Settings")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ").strip()
            if choice == '1':
                self.calculate()
            elif choice == '2':
                app_settings.set_decimal_places()

            elif choice == '3':
                break

            else:
                print("Invalid choice, please select a number between 1 and 3.")

