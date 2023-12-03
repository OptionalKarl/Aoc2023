import csv

def get_csv_file(file_path):
    try:
        mylist = []
        with open(file_path, 'r') as file:
            for line in file:
                mylist.append(line.strip())
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")