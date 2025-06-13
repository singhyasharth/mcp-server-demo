import pandas as pd
from typing import Optional
import os.path

def read_csv_file(file_path: str) -> Optional[pd.DataFrame]:
    """
    Read a CSV file and return its contents as a pandas DataFrame.
    Attempts multiple encodings to handle different file formats.
    
    Args:
        file_path (str): Path to the CSV file to be read
        
    Returns:
        pd.DataFrame: DataFrame containing the CSV data if successful
        None: If there was an error reading the file
    """
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"Successfully read file using {encoding} encoding")
            return df
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except pd.errors.EmptyDataError:
            print(f"Error: File '{file_path}' is empty.")
            return None
        except UnicodeDecodeError:
            continue  # Try next encoding
        except Exception as e:
            print(f"Error reading file '{file_path}' with {encoding} encoding: {str(e)}")
            continue  # Try next encoding
    
    print(f"Error: Could not read file '{file_path}' with any of the attempted encodings")
    return None
# Example: Reading the Aggregate Expenditure file
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'csv_files', 'Aggregate_Expenditure.csv')
df = read_csv_file(file_path)
if df is not None:
    print("First few rows of Aggregate Expenditure data:")
    print(df.head())