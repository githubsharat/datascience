# iNeuron Assignment Submission (Simple Inheritance)
# User submits assignment(s) on iNeuron.ai
# assignment class inherits from Account_Class class (imported from UserInfo module)

import logging
logging.basicConfig(filename='Assignment.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

from UserInfo import Account_Class

if __name__ == '__main__':
    class assignment(Account_Class):
        def __init__(self, title):
            '''title of  the assignment'''
            self.title = title
            self.count = 0

        def download(self):
            '''downloads the assignment from ineuron website'''
            logging.info(f"Assignment \"{self.title}\" downloaded")

        def upload(self, github_link):
            '''To post the GitHub link that has your response to the assignment'''
            self.github_link = github_link
            logging.info(f"Your GitHub link to \"{self.title}\" has been uploaded")

        def submit(self):
            '''To submit the assignment. It will confirm submission and prints no. of assignments submitted today'''
            count = 0
            self.count += 1
            from datetime import datetime
            now = datetime.now()
            logging.info(f"{self.title} has been submitted by {self.user_id} at {now}")
            logging.info(f"No. of assignments submitted today: {self.count}")


# user clicks on assignment_1 tab
assign1 = assignment("Assignment_1")

# checks validity of login credentials
assign1.login_check("user155@gmail.com", "passw33")  # Incorrect user ID

# checks validity of login credentials
assign1.login_check("user55@gmail.com", "passw33")  # User Logs in

# user downloads the assignment
assign1.download()

# user uploads GitHub link
assign1.upload("www.github.com/data/task1.ipynb")

# user submits the assignment
assign1.submit()