import logging
logging.basicConfig(filename='Task6_String.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

class string1:

    def __init__(self, s):
        self.s = s
        logging.info("Input: {}".format(self.s))

    def reverse_string(self):
        '''Method to reverse the string'''
        try:
            new_string = ""
            for i in range(len(self.s)):
                new_string = new_string + self.s[len(self.s) - i - 1]
            logging.info('Reversed: {}'.format(new_string))
            return new_string
        except Exception as e:
            logging.exception(e)

    def split_upper_string(self):
        '''' Method to split string after converting it to upper case '''
        try:
            s = self.s.upper().split()
            logging.info('Capitalized & Split: {}'.format(s))
            return s
        except Exception as e:
            logging.exception(e)

    def cap(self):
        '''Method to capitalize the whole string'''
        try:
            s = self.s.split()
            c = ''
            for i in s:
                c = c + ' ' + i.upper()
            logging.info('Capitalized: {}'.format(c))
            return c
        except Exception as e:
            logging.exception(e)

    def replace_string(self, current, new):
        '''Method to replace characters of a string'''
        try:
            new_string = self.s.replace(current,new)
            logging.info(f"Replaced ({current} with {new}): {new_string}" )
            return new_string
        except Exception as e:
            logging.exception(e)

    def lower1(self):
        """Method to convert the string to lower case"""
        try:
            s = self.s.lower()
            logging.info(f"Lower Case: {s}")
            return s
        except Exception as e:
            logging.exception(e)

    def slice1(self, start, end, step):
        """Slice the string with start, end, and step"""
        try:
            s = self.s[start:end:step]
            logging.info(f"Sliced: {s}")
            return s
        except Exception as e:
            logging.exception(e)


test_string = string1("HELLO There! good morning!")
test_string.lower1()
test_string.reverse_string()
test_string.split_upper_string()
test_string.cap()
test_string.replace_string("morning", "night")
test_string.slice1(0,5,1)










