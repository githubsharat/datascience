# iNeuron Hall of Fame (Simple Inheritance)
# User registers in ineuron's Hall of Fame portal.
# hall_of_fame class inherits from Account_Class class (imported from UserInfo module)

import logging
logging.basicConfig(filename='Hall_of_Fame.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

from UserInfo import Account_Class

if __name__ == '__main__':
    class hall_of_fame(Account_Class):
        def user_details(self, profile_pic, description):
            '''user's profile picture location and user's post description'''
            self.profile_pic = profile_pic
            self.description = description

        def linkedin(self, username, pass1):
            '''user needs to enter their linkedin username and password to validate it'''
            self.username = username
            self.pass1 = pass1
            logging.info("LinkedIn login successful")

        def preview(self):
            '''shows preview of the post'''
            logging.info(
                f"This is a preview of {self.name}\'s' post on Hall of Fame: {self.description}. Click \"Submit\" to post it.")

        def submit(self):
            '''submits the post for moderator approval'''
            logging.info(f"{self.name}, your post has been submitted to moderator for approval")


student1 = hall_of_fame()

# user enters their LinkedIn credentials
student1.linkedin("student25@linkedin.com", "password")

# check validity of ineuron login details
student1.login_check("user55@gmail.com", "passw33")

# user uploads profile picture (file path) and enter's description of the post
student1.user_details("C:\\Users\\User\\Desktop\\A123.jpg", "this is a test description")

# user previews their post before submitting it
student1.preview()

# user submits their post for moderator approval
student1.submit()    