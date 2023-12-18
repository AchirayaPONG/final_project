"""This is the main file for the project management system."""
import csv
import datetime
import os
import random
import time

from database import Database, Table

# define a function called initializing

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

db = Database()


# Member: Check member's project details in file project_table.csv


def exit_table():
    """Exit function for exit related activities"""
    for table in db.database:
        with open(os.path.join(__location__, table.table_name+'.csv'),
                  'w', encoding='utf-8') as f:
            rows = csv.writer(f)
            rows.writerow(table.get_table()[0].keys())
            for r in table.get_table():
                r: dict
                value_r = r.values()
                # {a: b, c: d}
                # [a, b, c, d, ...]
                rows.writerow(value_r)


class Member:
    """Member class for member related activities"""
    @staticmethod
    def check_project_id(user_id):
        """Check id in login.csv file and project_table.csv file

        if it is same then print project details.
        """
        with open(os.path.join(__location__, 'project_table.csv'), 'r',
                  encoding='utf-8') as f:
            rows = csv.DictReader(f)
            list_project = []
            for r in rows:
                if user_id == r.values():
                    list_project.append(dict(r))
            return list_project

    @staticmethod
    def modify_project_id():
        """Modify project id"""
        ask_user = input("Do you want to modify project details? (y/n): ")
        if ask_user == 'y':
            project_id = input("Enter project id: ")
            with open(os.path.join(__location__, 'project_table.csv')) as f:
                rows = csv.DictReader(f)
                for r in rows:
                    if r['ProjectID'] == project_id:
                        print('_' * 50)
                        print("Project details: ")
                        print('_' * 50)
                        print(f'Project project id: {r["ProjectID"]}')
                        print(f'Project title: {r["Title"]}')
                        print(f'Project lead: {r["Lead"]}')
                        print(f'Project member1: {r["Member1"]}')
                        print(f'Project member2: {r["Member2"]}')
                        print(f'Project advisor: {r["Advisor"]}')
                        print(f'Project status: {r["Status"]}')
                        print('_' * 50)
                        ask_user = input("Do you want to modify "
                                         "project details? (y/n): ")
                        print('_' * 50)
                        if ask_user == 'y':
                            print("** Enter new details **")
                            print('_' * 50)
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
                            print('_' * 50)
                            print("Project details updated successfully.")
                            print('_' * 50)
                            return True
                        else:
                            return False


class Admin:
    """Admin class for admin related activities"""
    def __init__(self, update, delete, add):
        self.update = update
        self.delete = delete
        self.add = add

    def update(self, primary_attribute, primary_attribute_value):
        """update the value of the primary attribute"""
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
    """Student class for student related activities"""
    def __init__(self, student_id):

        self.id = student_id
        self.invitation_status = None
        # None for no invitation, 'accepted',
        # or 'denied' for the respective status
        self.project_details = {}


    def see_invitation(self):
        """See invitation"""
        val_project = db.search('project_table').table
        # val_project shows all the project details in project_table.csv file
        # And it is in list of dictionary format [{}, {}, {}]
        print("." * 50)
        print("If you accept the invitation, "
              "you'll be part of the project from start to finish.")
        print("." * 50)
        for project in val_project:  # show dictionary of project details
            # {ProjectID: P001,..., Status: Completed}
            if self.id in project.values():
                print(f"You are already part of a project: {project['Title']}")
                print("_" * 50)


    def accept_or_deny(self):
        """Accept or deny invitation"""
        val_project = db.search('member_table').table
        for project in val_project:
            if self.id in project.values():  # check if student is in project
                if project['Response'] == 'Pending':
                    print("*" * 50)
                    print("The lead has invited you to join a project.")
                    print("*" * 50)
                    response = input("Would you like to accept the "
                                     "invitation? (y/n): ").lower()
                    print("_" * 50)
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
        """See project details"""
        if self.invitation_status == 'accepted':
            for key, value in self.project_details.items():
                print("_" * 50)
                print("___Project Details___\n")
                print(f"{key}: {value}")
        # if it's accepted, print the project details
        else:
            print("You haven't accepted an invitation to a project yet.")
        # if it's denied, print the message that the invitation is denied


    def modify_project_details(self):
        """Modify project details"""
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
                    print("Would you like to modify the project?")
                    response = \
                        input("Choose a number from the options above:")
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
                        break


class LeadStudent:
    """LeadStudent class for lead student related activities"""
    def __init__(self, lead_id, project_table, person_table,
                 member_request_table):
        self.id = lead_id
        self.project_details = {}
        self.group_members = []
        self.project_table = project_table
        self.person_table = person_table
        self.member_request_table: Table = member_request_table

    def show_information(self):
        """Show information"""
        while True:
            print("1. Create Project")
            print("2. Find Members")
            print("3. Send Invitations to Members")
            print("4. Add member to project")
            print("5. See & Modify Project Details")
            print("6. Send Advisor Request")
            print("7. Submit Final Report")
            print("8. Exit")
            print("_" * 50)
            choice = input("Enter your choice: ")
            print("_" * 50)
            if choice == '1':
                title = input("Enter project title: ")
                advisor = input("Enter advisor: ")
                self.create_project(title, advisor)
            elif choice == '2':
                self.find_members()
            elif choice == '3':
                self.send_invitations()
            elif choice == '4':
                self.add_member()
            elif choice == '5':
                self.see_project_details()
            elif choice == '6':
                advisor = input("Enter advisor: ")
                self.send_advisor_request(advisor)
            elif choice == '7':
                self.submit_final_report()
            elif choice == '8':
                break


    def create_project(self, title, advisor):
        """Create project"""
        while True:
            random_number = random.randint(1, 999)
            formatted_number = f"{random_number:03d}"
            random_primary_key = f"P{formatted_number}"
            if random_primary_key not in db.search('project_table').table:
                break

        self.project_details = {
            'ProjectID': random_primary_key,
            'Title': title,
            'Lead': self.id,
            'Advisor': advisor,
            'Status': 'In Progress'
        }

    def find_members(self):
        """Find members"""
        n = 1
        for project in self.project_table.table:
            if project['Lead'] == self.id:
                print(f"{n}. {project['Title']},"
                      f" Members: {project['Member1']}, {project['Member2']}")
                n += 1
        print("_" * 50)

    def send_invitations(self):
        """Send invitations to members"""
        for person in self.person_table.table:
            for project in self.project_table.table:
                if project['Lead'] == self.id:
                    if person['ID'] not in project.values():
                        self.member_request_table.insert(entry={
                            'ProjectID': project['ProjectID'],
                            'ToBeMember': person['ID'],
                            'Response': 'Pending',
                            'ResponseDate': datetime.date.today()
                        })
                        print(f"Invitation sent to {person['first']} "
                              f"{person['last']} "
                              f"for project {project['Title']}")
        print("_" * 50)

    def add_member(self):
        """Add member to project"""
        for project in self.project_table.table:
            if self.id == project['Lead']:
                if project['Member1'] == '':
                    project['Member1'] = input("Enter member1 ID: ")
                elif project['Member2'] == '':
                    project['Member2'] = input("Enter member2 ID: ")
                else:
                    print("This project is already full.")
                    print("_" * 50)
                    break

    def see_project_details(self):
        """See project details"""
        print("\nProject Details:")
        for key, value in self.project_details.items():
            print(f"{key}: {value}\n")

    def modify_project_details(self):
        """Modify project details"""
        print("_" * 50)
        ask_user = \
            input("Would you like to modify project details? (y/n): ").lower()
        if ask_user == 'y':
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
            print("Would you like to modify the project?\n")
            response = \
                input("Choose a number from the options above:")
            if response == '1':
                project_id = input("Enter new project ID: ")
                self.project_details['ProjectID'] = project_id
                print("Project ID updated successfully.")
            elif response == '2':
                project_title = input("Enter new project title: ")
                self.project_details['Title'] = project_title
                print("Project title updated successfully.")
            elif response == '3':
                project_lead = input("Enter new project lead: ")
                self.project_details['Lead'] = project_lead
                print("Project lead updated successfully.")
            elif response == '4':
                project_member1 = input("Enter new project member1: ")
                self.project_details['Member1'] = project_member1
                print("Project member1 updated successfully.")
            elif response == '5':
                project_member2 = input("Enter new project member2: ")
                self.project_details['Member2'] = project_member2
                print("Project member2 updated successfully.")
            elif response == '6':
                project_advisor = input("Enter new project advisor: ")
                self.project_details['Advisor'] = project_advisor
                print("Project advisor updated successfully.")
            elif response == '7':
                project_status = input("Enter new project status: ")
                self.project_details['Status'] = project_status
                print("Project status updated successfully.")
            elif response == '8':
                exit_table()
        else:
            print("Project details not modified.")

    def send_advisor_request(self, advisor):
        """Send advisor request"""
        print(f"Sending request to advisor {advisor}"
              f" for project "
              f"'{self.project_table.filter(lambda x: x['Lead'] == self.id).table[0]['Title']}'")
        # Logic to send a request to the advisor goes here
        print("_" * 50)
        print(f"Request sent to advisor {advisor}!")
        print("_" * 50)

    def submit_final_report(self):
        """Submit final report"""
        project = self.project_table.filter(lambda x: x['Lead'] == self.id)\
            .table[0]['Status'] == 'Completed'
        if project:
            submit = \
                input("Would you like to submit the final report? (y/n): ")
            if submit == 'y':
                self.project_details['Status'] = 'Completed'
                print("_" * 50)
                print(f"Submitting final project report for project"
                      f"{project}\n Please wait while we are"
                      f" loading...")
                # Logic to submit the final report goes here
                print(time.sleep(5))
                print("_" * 50)
                print("Final report submitted successfully, Thank you!")
                print("_" * 50)
        else:
            print('Project status is not completed yet!')



class NormalFaculty:
    """NormalFaculty class for normal faculty related activities"""
    def __init__(self, faculty_id):
        self.id = faculty_id

    def see_supervisor_requests(self, project_requests):
        """See supervisor requests"""
        if project_requests is None:
            print("_" * 50)
            print("Sorry, there are no requests for you at this time.")
            print("_" * 50)
        else:
            print("_" * 50)
            print(f"\nSupervisor Requests for {self.id}:")
            print("_" * 50)
            for request in project_requests:
                print(f"ProjectID: {request['ProjectID']},"
                      f" Title: {request['Title']},"
                      f" Student: {request['StudentName']}")


    def respond_to_request(self, project_id):
        """Respond to request"""
        response = input("Would you like to respond to the request? (y/n): ")

        if response == 'y':
            print("_" * 50)
            print(f"Responding to the "
                  f"request for project {project_id}: {response}")
            print("_" * 50)
            # Logic to respond to the request goes here
        elif response == 'n':
            print("_" * 50)
            print('Request denied.')
            print("_" * 50)
        else:
            print("_" * 50)
            print('Invalid response.')
            print("_" * 50)


    def view_all_projects(self, all_projects):
        """View all projects"""
        print("\nDetails of All Projects:")
        print("_" * 50)
        for project in all_projects.table:
            print(f"ProjectID: {project['ProjectID']},"
                  f" Title: {project['Title']},"
                  f" Advisor: {project['Advisor']}")
        print("_" * 50)

    def evaluate_projects(self, projects_to_evaluate):
        """Evaluate projects"""
        print("\nEvaluating Projects:")
        for project in projects_to_evaluate.table:
            # Placeholder logic for project evaluation,
            # you can expand on this based on your specific evaluation criteria
            evaluation_score = input(f"Enter evaluation score "
                                     f"for project {project['ProjectID']}: ")
            print(f"Project {project['ProjectID']} "
                  f"evaluated with a score of {evaluation_score}")


class AdvisingFaculty:
    """AdvisingFaculty class for advising faculty related activities"""
    def __init__(self, faculty_id):
        self.id = faculty_id
        self.normal_faculty = NormalFaculty(faculty_id)

    def see_supervisor_requests(self, project_requests):
        """See supervisor requests"""
        if self.normal_faculty.see_supervisor_requests(project_requests)\
                is not None:
            print("_" * 50)
            print("Would you like to respond to any of the requests?")
            print("_" * 50)
            response = input("Enter project ID to respond to the request: ")
            if response == 'y':
                print("_" * 50)
                print(f"Responding to the "
                      f"request for project {response}: {response}")
                print("_" * 50)
            else:
                print("_" * 50)
                print('Request denied.')
                print("_" * 50)
        else:
            print("_" * 50)
            print("Sorry, there are no requests for you at this time.")
            print("_" * 50)



    def send_accept_response(self, project_id):
        """Send acceptance response"""
        for project in project_id:
            if project['ProjectID'] == project_id:
                project['Status'] = 'Accepted'
                print(f"Sending acceptance response for project {project_id}")
        print(f"Sending acceptance response for project {project_id}")



    def send_deny_response(self, project_id):
        """Send denial response"""
        for project in project_id:
            if project['ProjectID'] == project_id:
                project['Status'] = 'Denied'
                print(f"Sending denial response for project {project_id}")
        print(f"Sending denial response for project {project_id}")


    def view_all_projects(self, all_projects):
        """View all projects"""
        print("\nDetails of All Projects:")
        for project in all_projects:
            print(f"ProjectID: {project['ProjectID']}, "
                  f"Title: {project['Title']}, Advisor: {project['Advisor']}")

    def evaluate_projects(self, projects_to_evaluate):
        """Evaluate projects"""
        print("\nEvaluating Projects:")
        for project in projects_to_evaluate:
            evaluation_score = random.randint(1, 10)
            # Placeholder for random evaluation score (customize as needed)
            print(f"Project {project['ProjectID']} "
                  f"evaluated with a score of {evaluation_score}")

    def approve_project(self, project_id):
        """Approve project"""
        if project_id['Status'] == 'Accepted':
            print(f"Project {project_id} approved!")
        else:
            print(f"Project {project_id} denied!")




def read_csv_data(filename):
    """Read csv file and return list of dictionary"""
    lst_db = []
    with open(os.path.join(__location__, filename),
              mode='r', encoding='utf-8') as f:
        rows = csv.DictReader(f)
        for r in rows:
            lst_db.append(dict(r))

    return lst_db


def initializing():
    """Initializing function for initializing database"""
    # Read all csv files
    read_person = read_csv_data('persons.csv')
    read_login = read_csv_data('login.csv')
    read_project_table = read_csv_data('project_table.csv')
    read_member_table = read_csv_data('member_table.csv')
    read_advisor_table = read_csv_data('advisor_table.csv')

    # print(read_person)
    person = Table('persons', read_person)
    login_data = Table('login', read_login)
    project_table = Table('project_table', read_project_table)
    member_table = Table('member_table', read_member_table)
    advisor_table = Table('advisor_table.csv', read_advisor_table)

    # Add all tables to the database
    db.insert(person)
    db.insert(login_data)
    db.insert(project_table)
    db.insert(member_table)
    db.insert(advisor_table)


# here are things to do in this function:

    # create an object to read all csv files
    # that will serve as a persistent state for this program

    # create all the corresponding tables for those csv files

    # see the guide how many tables are needed

    # add all these tables to the database

# define a function called login


def login():
    """Login function for login related activities"""
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
    MODIFY_PROJECT = member.modify_project_id()
    print(MODIFY_PROJECT)
    exit_table()
    # see and do member related activities
elif val[1] == 'lead':
    lead = LeadStudent(val[0],
                       db.search('project_table'),
                       db.search('persons'),
                       db.search('member_table'))

    lead.show_information()
    # see and do lead related activities
elif val[1] == 'faculty':
    faculty = NormalFaculty(val[0])
    faculty.see_supervisor_requests(db.search('member_request_table'))
    faculty.respond_to_request('project_id')
    faculty.view_all_projects(db.search('project_table'))
    faculty.evaluate_projects(db.search('project_table'))
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everything is done, make a call to the exit function
