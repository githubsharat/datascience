# New User Signs up and Logs in (Simple Inheritance)
# A new user signs up to join iNeuron.ai on the website and tries to log in
# account1 class inherits from iNeuron class

import logging
logging.basicConfig(filename='Signup.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

class iNeuron:
    def sign_up(self, fName, lName, user_id, phone, __password):
        '''captures user details needed for signing up on ineuron.ai'''
        self.fName = fName
        self.lName = lName
        self.user_id = user_id
        self.phone = phone
        self.__password = __password
        logging.info(f"Hello {fName}! Your user account has been created")

    def login_check(self, input_id, input_pass):
        '''validates login details entered by user'''
        try:
            self.loginid = input_id
            self.pass1 = input_pass
            if self.loginid == self.user_id and self.pass1 == self._iNeuron__password:
                logging.info(f"User {self.user_id} logged in successfully")
            else:
                logging.info("Login Failed! Please enter your login ID and password correctly")
        except Exception as e:
            logging.exception(e)


class account1(iNeuron):
    pass


####

student1 = account1()

# New user signs up on iNeuron.ai
student1.sign_up("Sharat", "A", "user55@gmail.com", "9949994999", "passw33")

# User enters wrong password
student1.login_check("sha@gmail.com", "password")  # Wrong Login

# User enters correct password
student1.login_check("user55@gmail.com", "passw33")  # Correct Login
