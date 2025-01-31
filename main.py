import os
from read_csv import (delete_blanc_rows, get_columns_names,read_all_file,write_csv,read_file_to_df,read_file_extracted,clean)
from db_postgres import db_conn

def save_raw_data_into_db():
    path = 'data_prueba_tecnica.csv'
    # erase blanc rows
    file = delete_blanc_rows(path)
    
    # get columns names
    names = get_columns_names(file).split(',') 

    
    create_script = f''' CREATE TABLE IF NOT EXISTS cargo (
                                    id varchar(50)NOT NULL,
                                    company_name varchar(40) NOT NULL,
                                    company_id varchar(50) NOT NULL,
                                    amount numeric(18,2) NOT NULL,
                                    status varchar(40) NOT NULL,
                                    created_at timestamp NOT NULL,
                                    paid_at timestamp NULL);'''

    # creates the table
    db_conn(create_script)
    
    # read the file
    file_to_load = read_all_file(file,nulls=True)

    insert_script = "INSERT INTO cargo(id, company_name, company_id, amount, status, created_at,paid_at) values(%s,%s,%s,%s,%s,%s,%s)"
    
    
    insert_values = (tuple(x) for x in file_to_load)
    
    #Inserting all values to db
    for _ in range(len(file_to_load)):
        try:
            db_conn(insert_script,next(insert_values))
        except StopIteration:
            pass
    print("Done")


def extract_information():
    new_file_name = None
    count_script = 'SELECT COUNT(*) FROM cargo'
    count = db_conn(count_script,select=True)
    count = int(next(count)[0])
    #print(count)

    select_script = 'SELECT * FROM cargo'
    fetch_data = db_conn(select_script,select=True)
    #print(fetch_data)
    try:
        for _ in range(count):
            new_file_name = write_csv(fetch_data)
    except StopIteration:
        pass
    return new_file_name


def load():
    create_script = f''' CREATE TABLE IF NOT EXISTS companies (
                                    company_name varchar(24) unique not null,
                                    company_id varchar(40) unique not null
                                    );'''

    # creates the table
    db_conn(create_script)

    create_script = f''' CREATE TABLE IF NOT EXISTS charges (
                                    id varchar(50) not null,
                                    company_name varchar(40) not null,
                                    company_id varchar(40) not null,
                                    amount numeric(18,2) NOT NULL,
                                    status varchar(40) NOT NULL,
                                    created_at timestamp NOT NULL,
                                    paid_at timestamp NULL,
                                    foreign key (company_name) references companies(company_name)
                                    on delete cascade);'''

    # creates the table
    db_conn(create_script)
    print("charges created")

    # get the unique names
    insert_script = "select distinct(company_name) ,company_id from cargo;"
    companies_ = db_conn(insert_script,select=True)
    file_to_load = read_all_file("clean.csv",nulls=True)
    
    insert_script = "INSERT INTO companies(company_name,company_id) values(%s,%s);"
    #Inserting companies to db
    for _ in range(len(file_to_load)):
        try:
            db_conn(insert_script,next(companies_))
        except StopIteration:
            pass
    print("Done")
    



    file_to_load_c = read_all_file("new.csv",nulls=True)
    # read the file
    insert_script_c = "INSERT INTO charges(id, company_name, company_id, amount, status, created_at,paid_at) values(%s,%s,%s,%s,%s,%s,%s);"
    
    insert_values_c = (tuple(x) for x in file_to_load_c)
    
    #Inserting all values to db
    for _ in range(len(file_to_load_c)):
        try:
            db_conn(insert_script_c,next(insert_values_c))
        except StopIteration:
            pass
    print("Done")
if __name__ == '__main__':
    os.system('clear')
    DROP_TABLE = 'DROP TABLE IF EXISTS cargo'

    db_conn(DROP_TABLE)

    # #save information
    save_raw_data_into_db()

    # ##### extract
    file_name = extract_information()
    
    result = read_file_extracted(file_name)
    
    print()    
    
    for i in range(len(result)):
        clean(result[i].split(','))

    # load
    DROP_TABLE_COMPANIES = 'DROP TABLE IF EXISTS companies'
    DROP_TABLE_CHARGES = 'DROP TABLE IF EXISTS charges'

    db_conn(DROP_TABLE_CHARGES)
    db_conn(DROP_TABLE_COMPANIES)
    load()
