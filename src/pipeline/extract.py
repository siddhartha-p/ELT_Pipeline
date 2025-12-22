import csv
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def extract_employees(csv_path: str):
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            first_line = f.readline()
            delimiter = '|' if '|' in first_line else ','
            f.seek(0)
            
            reader = csv.reader(f, delimiter=delimiter)
            headers = next(reader)
            rows = list(reader)
            
        logger.info(f"Extracted {len(rows)} employee records from {Path(csv_path).name}")
        return headers, rows
        
    except Exception as e:
        logger.error(f"Failed to extract employees: {e}")
        raise


def extract_timesheets(csv_path: str):
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            first_line = f.readline()
            delimiter = '|' if '|' in first_line else ','
            f.seek(0)
            
            reader = csv.reader(f, delimiter=delimiter)
            headers = next(reader)
            rows = list(reader)
            
        logger.info(f"Extracted {len(rows)} timesheet records from {Path(csv_path).name}")
        return headers, rows
        
    except Exception as e:
        logger.error(f"Failed to extract timesheets: {e}")
        raise


if __name__ == "__main__":
    # Update these paths to your actual CSV files
    employees_file = "../../data/employee_001.csv"
    timesheets_file = "../../data/timesheet_001.csv"
    
    # Extract employees
    emp_headers, emp_rows = extract_employees(employees_file)
    print(f"\nEmployees: {len(emp_rows)} rows, {len(emp_headers)} columns")
    print(f"Headers: {emp_headers}")
    print(f"First row: {emp_rows[0]}")
    
    # Extract timesheets
    ts_headers, ts_rows = extract_timesheets(timesheets_file)
    print(f"\nTimesheets: {len(ts_rows)} rows, {len(ts_headers)} columns")
    print(f"Headers: {ts_headers}")
    print(f"First row: {ts_rows[0]}")

