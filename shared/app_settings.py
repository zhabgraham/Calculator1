decimal_places = 0

def set_decimal_places():
    global decimal_places  
    while True:
        try:
            decimal_places = int(input('Enter number of decimal places: '))
            print(f"Number of decimal places set to {decimal_places}.")
            break
        except ValueError:
            print("Please enter a valid integer.")
