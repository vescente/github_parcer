def save_to_json(data, filename):
    import json
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def log_message(message):
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(message)

def handle_exception(e):
    import logging
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.error(f"An error occurred: {e}")