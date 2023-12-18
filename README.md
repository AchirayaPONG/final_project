# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv
  - projects_table.csv
  - members_table.csv
  - TODO.md
  - README.md
  - .gitignore
  - proposal.md
  - advisor_table.csv

** file.py have class what? **
and explain what each class does

#### database.py ####
class Database
Have 3 methods
- insert : insert data to csv file
- search : search data from csv file

class Table
Have 5 methods
- insert : insert data to csv file
- filter : filter data from csv file
- update : update data from csv file

#### project_manage.py ####
class Admin
- update_user : update user data
complete: 90%

class Student
- see_invitation : see invitation from project
- accept_or_deny : accept or deny invitation from project
- see_project_details : see project detail
- modify_project_details : modify project detail
complete: 100%

class Member
- check_project_details : check project detail
- modify_project_details : modify project detail
complete: 100%

class LeadStudent
-show_information : show project detail
-create_project : create project
-find_member : find member to join project
-add_member : add member to project
-see_project_details : see project detail
-modify_project_details : modify project detail
-send_advisor_request : send advisor request
-submit_final_report : submit final report
complete: 100%

class NormalFaculty
-see_request : see request from student
-send_response : send response to student
-see_project_details : see project detail
-evaluate_project : evaluate project
complete: 70%

class AdvisingFaculty
-see_request : see request from student
-send_response : send response to student
-see_project_details : see project detail
-evaluate_project : evaluate project
-approve_project : approve project
complete: 60%

----------------------------------------------

### Roles ###

`Admin`: Manages user accounts, projects, and evaluations.

`Student`: Accepts or denies project invitations, views project details, and modifies project details if accepted.

`Member`: Checks and modifies project details.

`Lead Student`: Manages project-related activities, invites members, and submits the final project report.

`Faculty`: Evaluates project requests and views project details.

`Advising Faculty`: Accepts or denies projects, evaluates projects, and approves projects.

### Functionality ###

* `Admin`
Update, delete, and add functionality for users.
Update information based on primary attributes.

* `Student`
Accept or deny project invitations.
View and modify project details.

* `Member`
Check and modify project details.

* `Lead Student`
Create projects.
Find and add members to projects.
See and modify project details.
Send advisor requests and submit the final report.

* `Faculty`
See requests to be supervisors.
Send responses to serve as advisors.
See details of all projects.
Evaluate projects.

* `Advising Faculty`
See requests to be supervisors.
Send accept or deny responses.
See details of all projects.
Evaluate and approve projects.

### Database ###
Files and Structure

`database.py`: Module for managing the database and tables.

`persons.csv`: CSV file containing user details.

`login.csv`: CSV file containing login credentials.

`project_table.csv`: CSV file containing project details.

`member_table.csv`: CSV file containing member details.

`project_manage.py`: Main module for the project.
___


# Run the program 
## Run the program by typing the following command in the terminal: 

```
python3 project_manage.py
```
or 
```
python project_manage.py
```
---

### Classes ###

| Roles            | Action                               | Method                 | Class           | Completion percentage |
|------------------|--------------------------------------|------------------------|-----------------|-----------------------|
| Admin            | Update                               | update                 | Admin           | 90%                   |
| Admin            | Display role admin in string format. | __str__                | Admin           | 90%                   |
| Student          | Accept or deny project invitations.  | accept_or_deny         | Student         | 100%                  |
| Student          | See invitation from project.         | see_invitation         | Student         | 100%                  |
| Student          | See project details.                 | see_project_details    | Student         | 100%                  |
| Student          | Modify project details.              | modify_project_details | Student         | 100%                  |
| Member           | Check project details.               | check_project          | Member          | 100%                  |
| Member           | Modify project details.              | modify_project         | Member          | 100%                  |
| Lead             | Create projects.                     | create_project         | Lead            | 100%                  |
| Lead             | Find and add members to projects.    | find_member            | Lead            | 100%                  |
| Lead             | Show project details.                | show_information       | Lead            | 100%                  |
| Lead             | Add member to project.               | add_member             | Lead            | 100%                  |
| Lead             | See project details.                 | see_project_details    | Lead            | 100%                  |
| Lead             | Modify project details.              | modify_project         | Lead            | 100%                  |
| Lead             | Send advisor requests.               | send_advisor_request   | Lead            | 100%                  |
| Lead             | Submit the final report.             | submit_final_report    | Lead            | 100%                  |
| Faculty          | See requests to be supervisors.      | see_request            | NormalFaculty   | 70%                   |
| Faculty          | Send responses to serve as advisors. | send_response          | NormalFaculty   | 70%                   |
| Faculty          | See details of all projects.         | see_project_details    | NormalFaculty   | 70%                   |
| Faculty          | Evaluate projects.                   | evaluate_project       | NormalFaculty   | 70%                   |
| Advising Faculty | See requests to be supervisors.      | see_request            | AdvisingFaculty | 60%                   |
| Advising Faculty | Send accept or deny responses.       | send_response          | AdvisingFaculty | 60%                   |
| Advising Faculty | See details of all projects.         | see_project_details    | AdvisingFaculty | 60%                   |
| Advising Faculty | Evaluate projects.                   | evaluate_project       | AdvisingFaculty | 60%                   |
| Advising Faculty | Approve projects.                    | approve_project        | AdvisingFaculty | 60%                   |
---