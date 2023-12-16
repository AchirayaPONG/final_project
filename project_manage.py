# import database module
import csv, os
from database import Table
from database import Database
# define a function called initializing

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

db = Database()


# Member: Check member's project details in file project_table.csv

def exit(file_name):
    global db
    with open(os.path.join(__location__, file_name+'.csv'), 'w') as f:
        rows = csv.writer(f)
        class_table: Table = db.search(file_name)
        rows.writerow(class_table.get_table()[0].keys())
        for r in class_table.get_table():
            r: dict
            value_r = r.values()
            # {a: b, c: d}
            # [a, b, c, d, ...]
            rows.writerow(value_r)


class Member:

    @staticmethod
    def check_project_id(user_id):
        """Check id in login.csv file and project_table.csv file

        if it is same then print project details.
        """
        with open(os.path.join(__location__, 'project_table.csv')) as f:
            rows = csv.DictReader(f)
            list_project = []
            for r in rows:
                if user_id == r.values():
                    list_project.append(dict(r))
            return list_project

    @staticmethod
    def modify_project_id(user_id):
        ask_user = input("Do you want to modify project details? (y/n): ")
        if ask_user == 'y':
            project_id = input("Enter project id: ")
            with open(os.path.join(__location__, 'project_table.csv')) as f:
                rows = csv.DictReader(f)
                for r in rows:
                    if r['ProjectID'] == project_id:
                        print("Project details: ")
                        print(f'Project project id: {r["ProjectID"]}')
                        print(f'Project title: {r["Title"]}')
                        print(f'Project lead: {r["Lead"]}')
                        print(f'Project member1: {r["Member1"]}')
                        print(f'Project member2: {r["Member2"]}')
                        print(f'Project advisor: {r["Advisor"]}')
                        print(f'Project status: {r["Status"]}')
                        ask_user = input("Do you want to modify "
                                         "project details? (y/n): ")
                        if ask_user == 'y':
                            print("Enter new details: ")
                            project_title = input("Enter project title: ")
                            project_lead = input("Enter project lead: ")
                            project_member1 = input("Enter project member1: ")
                            project_member2 = input("Enter project member2: ")
                            project_advisor = input("Enter project advisor: ")
                            project_status = input("Enter project status: ")
                            r['Title'] = project_title
                            r['Lead'] = project_lead
                            r['Member1'] = project_member1
                            r['Member2'] = project_member2
                            r['Advisor'] = project_advisor
                            r['Status'] = project_status
                            print("Project details updated successfully.")
                            return True
                        else:
                            return False


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


class Student:
    def __init__(self, student_id):
        self.id = student_id
        self.invitation_status = None
        # None for no invitation, 'accepted',
        # or 'denied' for the respective status
        self.project_details = {}

    def see_invitation(self):
        val_project = db.search('project_table').table
        # val_project shows all the project details in project_table.csv file
        # And it is in list of dictionary format [{}, {}, {}]
        for project in val_project:  # show dictionary of project details
            # {ProjectID: P001,..., Status: Completed}
            if self.id in project.values():
                print(f"You are already part of a project: {project['Title']}")


    def accept_or_deny(self):
        val_project = db.search('member_request_table').table
        for project in val_project:
            if self.id in project.values():  # check if student is in project
                if project['Response'] == 'Pending':
                    print("The lead has invited you to join a project.")
                    response = input("Would you like to accept the "
                                     "invitation? (y/n): ").lower()
                    if response == 'y':
                        self.invitation_status = 'accepted'
                        # update invitation status
                        print("Invitation accepted! Welcome to the project.")
                    else:
                        self.invitation_status = 'denied'
                        # update invitation status
                        print("Invitation denied. Sorry you won't be part of "
                              "the project.")


    def see_project_details(self):
        if self.invitation_status == 'accepted':
            for key, value in self.project_details.items():
                print(f"{key}: {value}")
        # if it's accepted, print the project details
        else:
            print("You haven't accepted an invitation to a project yet.")
        # if it's denied, print the message that the invitation is denied


    def modify_project_details(self):
        val_project = db.search('project_table').table
        if self.invitation_status == 'accepted':
            for project in val_project:  # show dictionary of project details
                if self.id in project.values():
                    # check if student is in project_table.csv file
                    print(f"Project details: {project}")
                    print("_" * 50)
                    print("1. Project ID\n")
                    print("2. Title\n")
                    print("3. Lead\n")
                    print("4. Member1\n")
                    print("5. Member2\n")
                    print("6. Advisor\n")
                    print("7. Status\n")
                    print("8. Exit\n")
                    print("_" * 50)
                    response = \
                        input("Would you like to modify the project?: ")
                    if response == '1':
                        project_id = input("Enter new project ID: ")
                        project['ProjectID'] = project_id
                        print("Project ID updated successfully.")
                    elif response == '2':
                        project_title = input("Enter new project title: ")
                        project['Title'] = project_title
                        print("Project title updated successfully.")
                    elif response == '3':
                        project_lead = input("Enter new project lead: ")
                        project['Lead'] = project_lead
                        print("Project lead updated successfully.")
                    elif response == '4':
                        project_member1 = input("Enter new project member1: ")
                        project['Member1'] = project_member1
                        print("Project member1 updated successfully.")
                    elif response == '5':
                        project_member2 = input("Enter new project member2: ")
                        project['Member2'] = project_member2
                        print("Project member2 updated successfully.")
                    elif response == '6':
                        project_advisor = input("Enter new project advisor: ")
                        project['Advisor'] = project_advisor
                        print("Project advisor updated successfully.")
                    elif response == '7':
                        project_status = input("Enter new project status: ")
                        project['Status'] = project_status
                        print("Project status updated successfully.")
                    elif response == '8':
                        exit('project_table')



# Example Usage:
# student1 = Student(9898118, 'Lionel', 'Messi')
# lead_name = 'Robert Lewandowski'
# project_details = {
#     'ProjectID': 'P002',
#     'Title': 'Marketing Campaign',
#     'Lead': lead_name,
#     'Member1': 'Gareth Bale',
#     'Member2': 'Sergio Ramos',
#     'Advisor': 'Dr. Jennifer Lee',
#     'Status': 'Completed'
# }
#
# student1.receive_invitation(lead_name)
# student1.invitation_status()


def read_csv_data(filename):
    lst_db = []
    with open(os.path.join(__location__, filename)) as f:
        rows = csv.DictReader(f)
        for r in rows:
            lst_db.append(dict(r))

    return lst_db


def initializing():
    global db
    # Read all csv files
    read_person = read_csv_data('persons.csv')
    read_login = read_csv_data('login.csv')
    read_project_table = read_csv_data('project_table.csv')
    read_member_request = read_csv_data('member_request_table.csv')
    # print(read_person)
    person = Table('persons', read_person)
    login_data = Table('login', read_login)
    project_table = Table('project_table', read_project_table)
    member_request_table = Table('member_request_table', read_member_request)

    db.insert(person)
    db.insert(login_data)
    db.insert(project_table)
    db.insert(member_request_table)


# here are things to do in this function:

    # create an object to read all csv files
    # that will serve as a persistent state for this program

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


# here are things to do in this function:
# write out all the tables that have been modified-
# to the corresponding csv files.
# By now, you know how to read in a csv file and-
# transform it into a list of dictionaries.
# For this project, you also need to know how to do the reverse,-
# i.e., writing out to a csv file given a list of dictionaries.
# See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()
print(val)

# based on the return value for login, activate the code that
# performs activities according to the role defined for that person_id

if val[1] == 'admin':
    pass
    # see and do admin related activities
elif val[1] == 'student':
    student = Student(val[0])
    student.see_invitation()
    student.accept_or_deny()
    student.see_project_details()
    student.modify_project_details()
    # see and do student related activities
elif val[1] == 'member':
    member = Member()
    check_project = member.check_project_id(val[0])
    print(check_project)
    modify_project = member.modify_project_id(val[0])
    print(modify_project)
    exit('project_table')
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everything is done, make a call to the exit function


