from shared import memory, history

def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /, ^, sqrt, %): ").strip()
        if operator in ['+', '-', '*', '/', '^', 'sqrt', '%']:
            return operator
        print("Invalid operator! Please enter a valid operator.")


def get_operand(prompt):
    while True:
        value = input(prompt).strip()
        if value.upper() == 'MR':
            return memory.recall_memory()
        try:
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a valid number or 'MR'.")


def perform_memory_operation(result):
    memory_choice = input("Do you want to perform any memory operations (MS, M+, MC)? ").strip().upper()
    if memory_choice == 'MS':
        memory.save_to_memory(result)
    elif memory_choice == 'M+':
        memory.add_to_memory(result)
    elif memory_choice == 'MC':
        memory.clear_memory()


def perform_history_operation():
    history_choice = input("Do you want to view history? (yes/no) ").strip().lower()
    if history_choice == 'yes':
        history.show_history()

