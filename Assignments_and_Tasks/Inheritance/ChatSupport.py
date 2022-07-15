# iNeuron Chat Support (Multi Layer Inheritance)
# User tries chat support
# user class inherits from chat_support class, which inherits from Account_Class class (imported from UserInfo module)
# and chat_window class.

import logging
logging.basicConfig(filename='ChatSupport.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

from UserInfo import Account_Class

if __name__ == "__main__":
    class chat_window:
        def __init__(self, name, email, phone, dept=None):
            '''name of the user, user's email, and user's phone number. Department field is optional'''
            self.name = name
            self.email = email
            self.phone = phone
            self.dept = dept

    class chat_support(Account_Class, chat_window):
        def __init__(self, name, email, phone, dept=None):
            '''name of the user, user's email, and user's phone number. Department field is optional'''
            chat_window.__init__(self, name, email, phone, dept=None)

        def start(self):
            '''starts the chat with ineuron support'''
            logging.info(f"Hello {self.name}, welcome to iNeuron chat support. Please enter your query.")

        def end(self):
            '''end the chat with ineuron support'''
            logging.info("Your chat has been ended. Please rate the support.")

    class user(chat_support):
        pass


####

# user enter their details on chat support window, The last argument is optional.
user1 = user("Sharat", "user55@gmail.com", "9949994999", "Data Consultancy Team")

# check validity of login credentials
user1.login_check("user55@gmail.com", "passw33")

# start support chat
user1.start()

# end support chat
user1.end()