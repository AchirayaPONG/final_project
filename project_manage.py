# import database module
import csv, os
from database import Table
from database import Database
# define a function called initializing

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

db = Database()


def read_csv_data(filename):
    lst_db = []
    with open(os.path.join(__location__, filename)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            lst_db.append(dict(r))

    return lst_db


def initializing():
    global db
    read_person = read_csv_data('persons.csv')
    read_login = read_csv_data('login.csv')

    person = Table('person', read_person)
    login_data = Table('login', read_login)

    db.insert(person)
    db.insert(login_data)


# here are things to do in this function:

    # create an object to read all csv files that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database

# define a funcion called login


def login():
    global db
    user_name = input("ENTER USERNAME: ")
    pass_word = input("ENTER PASSWORD: ")

    check_username = lambda x: x['username'] == user_name
    check_password = lambda X: X['password'] == pass_word

    search_login = db.search('login')
    # print(search_login)
    #
    for check_data in search_login.get_table():
        # print(check_data)
        if check_username(check_data) and check_password(check_data):
            return [check_data['ID'], check_data['role']]
    return None

# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None

# define a function called exit
def exit():
    global db
    lst = []
    with open(os.path.join(__location__, 'persons.csv'), 'w') as f:
        rows = csv.writer(f)
        rows.writerow(['1', '2'])
        class_table: Table = db.search('person')
        for r in class_table.get_table():
            r: dict
            value_r = r.values()
            # {a: b, c: d}
            # [a, b, c, d, ...]
            rows.writerow(value_r)

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files
   # By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

   # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
