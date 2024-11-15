import logging

# Configure logging to log errors into a file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

def process_file(file_path):
    try:
        # Try to open the file - note just a simulation 
        with open(file_path, 'r') as file:
            data = file.readlines()

        # Simulate a data processing task
        processed_data = []
        for line in data:
            # Attempt to convert data to an integer, log an error if it fails
            try:
                number = int(line.strip())
                processed_data.append(number)
            except ValueError as e:
                logging.error(f"Error processing line '{line.strip()}': {e}")
                continue  # Skip this line and continue processing other data

        return processed_data

    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path} - {e}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

# Example usage
file_path = 'testfile.txt'  # This should be a file path to test
processed_data = process_file(file_path)

if processed_data is not None:
    print("Data processed successfully:", processed_data)
else:
    print("An error occurred during processing.")
