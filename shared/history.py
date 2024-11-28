import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

_history = []

def add_to_history(record):
    _history.append(record)
    logging.info(f"Added to history: {record}")

def show_history():
    if not _history:
        logging.info("History is empty.")
        print("History is empty.")
        return
    logging.info("Showing history:")
    print("History:")
    for record in _history:
        print(record)
