# iNeuron Affiliate Program (Multiple Inheritance)
# User joins iNeuron's affiliate program
# affiliate class inherits from bank_details class and Account class (imported from UserInfo module)

import logging
logging.basicConfig(filename='Affiliate.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

from UserInfo import Account_Class

if __name__ == '__main__':
    class bank_details:
        def __init__(self, bank_Account_no, Account_holder_name, IFSC_code, PAN_card_no):
            '''bank Account number, Account holder name, IFSC code, PAN card number'''
            self.bank_Account_no = bank_Account_no
            self.Account_holder_name = Account_holder_name
            self.IFSC_code = IFSC_code
            self.PAN_card_no = PAN_card_no

        def validate(self):
            '''validates bank Account details submitted by the user'''
            logging.info(f"Bank Account details validated for {self.user_id}")

    class affiliate(Account_Class, bank_details):
        def __init__(self, bank_Account_no, Account_holder_name, IFSC_code, PAN_card_no):
            '''bank Account number, Account holder name, IFSC code, PAN card number'''
            bank_details.__init__(self, bank_Account_no, Account_holder_name, IFSC_code, PAN_card_no)

        def create_affiliate(self):
            '''creates affilate link for the user'''
            logging.info(f"Affiliate link generated. Please use this link for referrals: {self.sample_link}")

# user fills compulsory banking information in the affilate form in  the portal
affiliate1 = affiliate("324511", "Ram Sharma", "2332111", "AA224355")

# check login details validity
affiliate1.login_check("test", "test")

# check login details validity
affiliate1.login_check("user55@gmail.com", "passw33")

# check validity of banking details
affiliate1.validate()

# create affiliate link for the user
affiliate1.create_affiliate()