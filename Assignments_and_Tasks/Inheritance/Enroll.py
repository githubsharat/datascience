# Simple Inheritance - iNeuron's Course Enrollment
# Enrolling an iNeuron user in new courses
# account class inherits from iNeuron class
import logging
logging.basicConfig(filename='Enroll.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

class iNeuron:
    def __init__(self, course, day, time, location):
        '''course name, training day, training time, training location'''
        self.course = course
        self.day = day
        self.time = time
        self.location = location
        self.courses = [course]

    def add_courses(self, *courses):
        try:
            self.courses = list(set(self.courses + list(courses)))  # set is used to remove duplicates
            logging.info(f"{self.name} has been enrolled in  the following courses: {self.courses}")
        except Exception as e:
            logging.exception(e)

class account(iNeuron):
    def __init__(self, name, user_id, course, day, time, location):
        '''name of the user, user id, course name, training day, training time, training location'''
        super().__init__(course, day, time, location)
        self.name = name
        self.user_id = user_id


s1 = account('Sharat', 'sa1@gmail.com', 'FSDS', 'Sat & Sun', '3pm to 6pm IST', 'Online')
s1.add_courses('Big Data Boot Camp', 'Full Stack Web Development')