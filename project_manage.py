# import database module
import csv, os
from database import Table
from database import Database
# define a function called initializing

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

db = Database()


# Member: Check member's project details in file project_table.csv

def check_project_id(user_id):
    """Check id in login.csv file and project_table.csv file

    if it is same then print project details.
    """
    with open(os.path.join(__location__, 'project_table.csv')) as f:
        rows = csv.DictReader(f)
        list_project = []
        for r in rows:
            if r['Lead'] == user_id or r['Member1'] == user_id\
                    or r['Member2'] == user_id:
                list_project.append(dict(r))
        return list_project


class Admin:
    def __init__(self, update, delete, add):
        self.update = update
        self.delete = delete
        self.add = add

    def update(self, primary_attribute, primary_attribute_value):
        lst_update = []
        with open(os.path.join(__location__, 'login.csv')) as f:
            rows = csv.writer(f)
            for r in primary_attribute and primary_attribute_value in rows:
                r: dict
                update_value = r.values()
                rows.writerow(update_value)
                update_attribute = r.keys()
                rows.writerow(update_attribute)
                lst_update.append(update_attribute)
                lst_update.append(update_value)
        return lst_update



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
    with open(os.path.join(__location__, 'persons.csv'), 'w') as f:
        rows = csv.writer(f)
        class_table: Table = db.search('person')
        rows.writerow(class_table.get_table()[0].keys())
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

if val[1] == 'admin':
    pass
    # see and do admin related activities
elif val[1] == 'student':
    pass
    # see and do student related activities
elif val[1] == 'member':
    data = check_project_id(user_id=val[0])
    for dict_of_project in data:
        print(f'Project project id: {dict_of_project["ProjectID"]}')
        print(f'Project title: {dict_of_project["Title"]}')
        print(f'Project lead: {dict_of_project["Lead"]}')
        print(f'Project member1: {dict_of_project["Member1"]}')
        print(f'Project member2: {dict_of_project["Member2"]}')
        print(f'Project advisor: {dict_of_project["Advisor"]}')
        print(f'Project status: {dict_of_project["Status"]}')
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
