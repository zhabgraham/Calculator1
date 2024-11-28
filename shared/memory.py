import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

_memory = None

def save_to_memory(value):
    global _memory
    _memory = value
    logging.info(f"Stored {value} in memory.")
    print(f"Stored {value} in memory.")


def add_to_memory(value):
    global _memory
    if _memory is not None:
        _memory += value
        logging.info(f"Added {value} to memory. New memory: {_memory}")
        print(f"Added {value} to memory. New memory: {_memory}")
    else:
        _memory = value
        logging.info(f"No previous memory. Stored {value} in memory.")
        print(f"No previous memory. Stored {value} in memory.")


def clear_memory():
    global _memory
    _memory = None
    logging.info("Memory cleared.")
    print("Memory cleared.")


def recall_memory():
    if _memory is not None:
        logging.info(f"Recalled memory: {_memory}")
        print(f"Recalled memory: {_memory}")
        return _memory
    logging.info("Memory is empty.")
    print("Memory is empty.")
    return None
