# Contact Support Function (Multiple Inheritance)
# User clicks on "contact us" on iNeuron.ai
# info class inherits from support class and course class

import logging
logging.basicConfig(filename='ContactUs.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

class course:
    course1 = 'FSDS'

class support:
    email = "query@ineuron.com"

class info(support, course):
    def __init__(self, name):
        '''captures name of the user'''
        self.name = name

    def help1(self):
        '''prints support email address to user'''
        try:
            logging.info(
                f"Hello {self.name}! Please contact iNeuron support at {support.email} for help with {course.course1} course")
        except Exception as e:
            logging.exception(e)


student1 = info("John")
student1.help1()