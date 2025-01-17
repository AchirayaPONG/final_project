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


#### database.py ####
class Database
Have 3 methods
- `insert` : insert data to csv file
- `search `: search data from csv file
- `__init__`   : create csv file

class Table
Have 5 methods
- `__init__` : create csv file
- `insert` : insert data to csv file
- `filter `: filter data from csv file
- `update` : update data from csv file
- `__str__ `: display data from csv file in string format
- `get_table `: get data from csv file

#### project_manage.py ####
class Admin
- update_user : update the value of the primary attribute

class Student
- see_invitation : see invitation from project
- accept_or_deny : accept or deny invitation from project
- see_project_details : see project details
- modify_project_details : modify project details

class Member
- check_project_id : check project details
- modify_project_id : modify project details

class LeadStudent
- show_information : show project details
- create_project : create project
- find_members : find members to join project
- send_invitations : send invitation to member
- add_member : add member to project
- see_project_details : see project details
- modify_project_details : modify project details
- send_advisor_request : send advisor request
- submit_final_report : submit final report

class NormalFaculty
- see_supervisor_requests : see supervisor requests
- respond_to_requests : respond to supervisor requests
- view_all_projects : view all projects
- evaluate_projects : evaluate projects

class AdvisingFaculty
- see_supervisor_requests : see supervisor requests
- send_accept_response : send accept response
- send_deny_response : send deny response
- view_all_projects : view all projects
- evaluate_projects : evaluate projects
- approve_project : approve project

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

### Classes Database ###

| Action                    | Method    | Class    | Completion percentage |
|---------------------------|-----------|----------|-----------------------|
| Insert data to csv file   | insert    | Database | 100%                  |
| Search data from csv      | search    | Database | 100%                  |
| Create csv file           | __init__  | Database | 100%                  |
| Create csv file           | __init__  | Table    | 100%                  |
| Insert data to csv file   | insert    | Table    | 100%                  |
| Filter data from csv file | filter    | Table    | 100%                  |
| Update data from csv file | update    | Table    | 100%                  |
| Display data from csv     | __str__   | Table    | 100%                  |
| Get data from csv         | get_table | Table    | 100%                  |
---

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

### Classes Project manage ###

| Roles            | Action                                     | Method                  | Class           | Completion percentage |
|------------------|--------------------------------------------|-------------------------|-----------------|-----------------------|
| Admin            | Update the value of the primary attribute. | update                  | Admin           | 90%                   |
| Admin            | Display role admin in string format.       | __str__                 | Admin           | 90%                   |
| Student          | Accept or deny project invitations.        | accept_or_deny          | Student         | 100%                  |
| Student          | See invitation from project.               | see_invitation          | Student         | 100%                  |
| Student          | See project details.                       | see_project_details     | Student         | 100%                  |
| Student          | Modify project details.                    | modify_project_details  | Student         | 100%                  |
| Member           | Check project details.                     | check_project_id        | Member          | 100%                  |
| Member           | Modify project details.                    | modify_project_id       | Member          | 100%                  |
| Lead             | Create projects.                           | create_project          | Lead            | 100%                  |
| Lead             | Find members in the project.               | find_members            | Lead            | 100%                  |
| Lead             | Show project details.                      | show_information        | Lead            | 100%                  |
| Lead             | Add member to project.                     | add_member              | Lead            | 100%                  |
| Lead             | Send invitation to member.                 | send_invitations        | Lead            | 100%                  |
| Lead             | See project details.                       | see_project_details     | Lead            | 100%                  |
| Lead             | Modify project details.                    | modify_project_details  | Lead            | 100%                  |
| Lead             | Send advisor requests.                     | send_advisor_request    | Lead            | 100%                  |
| Lead             | Submit the final report.                   | submit_final_report     | Lead            | 100%                  |
| Faculty          | See supervisor requests.                   | see_supervisor_requests | NormalFaculty   | 70%                   |
| Faculty          | Respond to supervisor request.             | respond_to_request      | NormalFaculty   | 70%                   |
| Faculty          | View all projects.                         | view_all_projects       | NormalFaculty   | 70%                   |
| Faculty          | Evaluate projects.                         | evaluate_projects       | NormalFaculty   | 70%                   |
| Advising Faculty | create csv file.                           | see_supervisor_requests | AdvisingFaculty | 60%                   |
| Advising Faculty | Send accept response.                      | send_accept_response    | AdvisingFaculty | 60%                   |
| Advising Faculty | Send deny response.                        | send_deny_response      | AdvisingFaculty | 60%                   |
| Advising Faculty | View all projects.                         | view_all_projects       | AdvisingFaculty | 60%                   |
| Advising Faculty | Evaluate projects.                         | evaluate_projects       | AdvisingFaculty | 60%                   |
| Advising Faculty | Approve project.                           | approve_project         | AdvisingFaculty | 60%                   |
---
