import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def addition(first_operand, second_operand):
    logging.debug(f"Performing addition: {first_operand} + {second_operand}")
    return first_operand + second_operand


def subtraction(first_operand, second_operand):
    logging.debug(f"Performing subtraction: {first_operand} - {second_operand}")
    return first_operand - second_operand


def multiplication(first_operand, second_operand):
    logging.debug(f"Performing multiplication: {first_operand} * {second_operand}")
    return first_operand * second_operand


def division(first_operand, second_operand):
    if second_operand == 0:
        logging.error("Division by zero attempted!")
        raise ValueError("Division by zero is not allowed.")
    logging.debug(f"Performing division: {first_operand} / {second_operand}")
    return first_operand / second_operand


def power(first_operand, second_operand):
    logging.debug(f"Performing power operation: {first_operand} ^ {second_operand}")
    return first_operand ** second_operand


def square_root(first_operand):
    if first_operand < 0:
        logging.error(f"Cannot calculate square root of a negative number: {first_operand}")
        raise ValueError("Cannot calculate square root of a negative number.")
    logging.debug(f"Performing square root: √{first_operand}")
    return first_operand ** 0.5


def modulus(first_operand, second_operand):
    logging.debug(f"Performing modulus operation: {first_operand} % {second_operand}")
    return first_operand % second_operand


def perform_operation(operator, first_operand, second_operand=None):
    logging.info(f"Operation started: {operator} with operands {first_operand}, {second_operand}")
    operations = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division,
        '^': power,
        'sqrt': square_root,
        '%': modulus,
    }
    operation = operations.get(operator)
    if operation:
        try:
            if operator == 'sqrt':
                result = operation(first_operand)
            else:
                result = operation(first_operand, second_operand)
            logging.info(f"Operation result: {result}")
            return result
        except Exception as e:
            logging.error(f"Error during operation {operator}: {e}")
            raise
    else:
        logging.error(f"Unsupported operator: {operator}")
        raise ValueError(f"Unsupported operator: {operator}")
