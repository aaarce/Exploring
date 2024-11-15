#simple logging error concept snippet 
import pandas as pd 
import logging

logging.basicConfig(level=logging.INFO)



try:
    # Attempt to load the CSV file
    df = pd.read_csv('data.csv')
    
    # Log that the data was loaded successfully
    logging.info("Data loaded successfully")
    
    # Check if the data is loaded and preview the first few rows
    logging.info(f"Data preview:\n{df.head()}")
    
except FileNotFoundError:
    logging.error("File not found!")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")