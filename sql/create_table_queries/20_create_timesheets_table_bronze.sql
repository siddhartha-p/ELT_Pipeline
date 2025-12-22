CREATE table bronze.timesheets (
    client_employee_id	VARCHAR,
    department_id VARCHAR,
    department_name	VARCHAR,
    home_department_id	VARCHAR,
    home_department_name VARCHAR,
    pay_code VARCHAR,	
    punch_in_comment VARCHAR,	
    punch_out_comment VARCHAR,
    hours_worked VARCHAR,	
    punch_apply_date VARCHAR,	
    punch_in_datetime VARCHAR,	
    punch_out_datetime VARCHAR,	
    scheduled_start_datetime VARCHAR,	
    scheduled_end_datetime VARCHAR,
    loaded_at TIMESTAMP,
    source_file VARCHAR
);