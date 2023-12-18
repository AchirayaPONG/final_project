### Project Planning

#### Project Overview:
The final project aims to develop a Python program in an object-oriented style to facilitate the administrative process of senior projects involving students, faculty, and admin. The key elements include managing persons, documents (specifically senior project reports), and their relationships.

#### Person Types:
1. **Student:**
   - *Roles:*
     - Lead (Heads the project)
     - Member (Part of the project under the lead)
     - Regular Student (Not yet a member of any project)
   - *Interactions:*
     - Sees invitational messages.
     - Accepts or denies invitations.
     - Views and modifies personal project details.

2. **Faculty:**
   - *Roles:*
     - Advisor (Supervises a project)
     - Regular Faculty (Does not supervise any project)
   - *Interactions:*
     - Sees requests to be a supervisor.
     - Responds to requests, either accepting or denying.
     - Views details of all projects.
     - Evaluates projects (more details in proposal).
     - Approves projects.

3. **Admin:**
   - *Roles:*
     - Manages the database.
     - Can update all tables.

#### Document Type:
- Senior Project Report

#### Overall Process:
1. Lead student proposes an interesting project.
2. Lead student forms a group by inviting at most two members.
3. The group searches for an advisor to supervise the project.
4. The advisor agrees to supervise the project.
5. The group submits a project proposal to the advisor.
6. The advisor approves the proposal.
7. Upon project completion, the group submits the project report to the advisor.
8. The advisor approves the final project.

#### Interactions:

##### Admin:
- Manages the database.
- Can update all tables.

##### Student:
- Sees invitational messages.
- Accepts or denies invitations.
- Views and modifies personal project details.

##### Lead Student:
- Creates a project.
- Finds members.
- Sends invitational messages.
- Adds members to the project.
- Views and modifies personal project details.
- Sends requests to potential advisors.
- Submits the final project report.

##### Member Student:
- Views and modifies personal project details.

##### Normal Faculty (Not an Advisor):
- Sees requests to be a supervisor.
- Sends responses denying to serve as an advisor.
- Views details of all projects.
- Evaluates projects (more details in proposal).

##### Advising Faculty:
- Sees requests to be a supervisor.
- Sends accept responses (for projects serving as an advisor).
- Sends deny responses (for projects not serving as an advisor).
- Views details of all projects.
- Evaluates projects (more details in proposal).
- Approves projects.

### Next Steps:
- Develop a detailed proposal outlining project structure, classes, methods, and interactions.
- Begin implementing the program following the proposed structure.
- Regularly test and debug the program to ensure smooth functionality.
- Continuously refer to the proposal to guide development.
- Implement any additional features or refinements as needed.