import csv
import os

def write_to_csv(data_dict : dict, csv_filename: str):
    """Creates a .csv to commit the response of the API.\n
    If .csv already exists,it appends the response as a new row.

    """
    
    
    # Check if the CSV file exists
    file_exists = os.path.isfile(csv_filename)
    
    with open(csv_filename, mode='a', newline='', encoding='utf-8') as csv_file:
        fieldnames = data_dict.keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        # Write header row if the file is being created for the first time
        if not file_exists:
            writer.writeheader()
        
        # Append the new data
        writer.writerow(data_dict)