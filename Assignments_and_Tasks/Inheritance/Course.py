# iNeuron's Course Enrollment (Multi Level Inheritance)
# User enrolls in various iNeuron training programs
# student class inherits from coaching class, which inherits from iNeuron_mentors class

import logging
logging.basicConfig(filename='Course.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

class iNeuron_mentors:
    def __init__(self, iName, hours):
        '''captures name of ineuron mentor and training timings'''
        self.iName = iName
        self.hours = hours
        self.trainings = []

    def add_trainings(self, *training):
        '''creates a list of trainings passed as argument'''
        try:
            self.trainings = list(set(self.trainings + list(training)))
            logging.info(f"Enrolled {self.sName} in the following courses: {self.trainings}")
        except Exception as e:
            logging.exception(e)

class coaching(iNeuron_mentors):
    def __init__(self, iName, hours, course, total_students):
        '''captures instructor name, course timings, course name and total students in the course'''
        super().__init__(iName, hours)
        self.course = course
        self.total_students = total_students

class student(coaching):
    def __init__(self, sName, iName, hours, course, total_students):
        '''student name, instructor name, course timings, course title, total students enrolled in the course'''
        super().__init__(iName, hours, course, total_students)
        self.sName = sName


Sharat = student("Sharat", "Sudhanshu", "3PM to 6PM", "FSDS", 200)
Sharat.add_trainings("FSDS", "Web Development")