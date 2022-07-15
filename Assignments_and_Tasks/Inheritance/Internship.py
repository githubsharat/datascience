# iNeuron Internship Portal (Multiple Inheritance)
# User registers in iNeuron Internship Portal
# Multiple Inheritance: internship class inherits from Account_Class class (imported from UserInfo module) and...
# project class

import logging
logging.basicConfig(filename='Internship.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

from UserInfo import Account_Class

if __name__ == '__main__':
    class project:
        def __init__(self, tech, domain):
            '''project technology, project domain'''
            self.tech = tech
            self.domain = domain
            self.projects = []

        def add_project(self, *projects):
            '''prepares a list of projects'''
            try:
                self.projects = list(set(self.projects + list(projects)))
                logging.info(f"Projects enrolled by {self.user_id}: {self.projects}")
            except Exception as e:
                logging.exception(e)

    class internship(Account_Class, project):
        def __init__(self, tech, domain, approved_by):
            '''project technology, project domain, project approved by'''
            project.__init__(self, tech, domain)
            self.approved_by = approved_by


# user enters mandatory fields in the internship form
internship1 = internship("Machine Learning", "Banking", "Supervisor")

# check validity of login credentials
internship1.login_check("john@gmail.com", "john123")  # Check login information

# enroll user in an internship project
internship1.add_project("Credit Card Default Prediction")  # Enroll a project

# enroll user in another internship project
internship1.add_project("Fraud Transaction Detection")  # Enroll another project