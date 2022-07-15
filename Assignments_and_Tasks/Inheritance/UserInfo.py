import logging

class Account_Class:
    user_id = "user55@gmail.com"
    __password = "passw33"
    name = "Sharat"
    phone = "9949994999"
    sample_link = "https://affiliate.ineuron.ai"

    def login_check(self, input_id, input_pass):
        '''validates login details entered by user'''
        self.loginid = input_id
        self.pass1 = input_pass
        try:
            if self.loginid == self.user_id and self.pass1 == self._Account_Class__password:
                logging.info(f"User {self.user_id} logged in successfully")
            else:
                logging.info("Login Failed! Please enter your login ID and password correctly")
        except Exception as e:
            logging.exception(e)


