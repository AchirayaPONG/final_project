database.py
Have two classes
-Database class 
-Table class 

About Database class have...
- Attribute:
database
- Method:
insert (add the table into the database)
search (searching for a table: If table.table_name equal to table_name, return table. If it's not return None)

About Table class have...
- Attribute:
table_name
table
- Method:
insert (append in entry)
filter (filter the table)
update (update the information)
__str__(magic method: to write the string)
get_table (getter)

project_manage.py
Have 4 functions

- read_csv_data(filename)
    To read database.py file
-  initializing()
     Create two tables to initialize the database. Using person.csv and
 login.csv file 

- login() 
    To check username and password and if it's equal to the data return ID and role.

- exit ()
    To update the person.csv the new information.
