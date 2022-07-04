import logging

logging.basicConfig(filename='Task6_List.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')


class list1:

    def __init__(self, l):
        self.l = l
        logging.info(f"Input: {l}")

    def reverse_list(self):
        '''Reverses list'''
        try:
            self.l.reverse()
            logging.info(f"Reversed: {l}")
            return l
        except Exception as e:
            logging.exception(e)

    def key_elements(self):
        '''Prints key elements for every dictionary in the list'''
        try:
            keys1 = []
            for i in self.l:
                if type(i) == dict:
                    keys1.append(i.keys())
            logging.info(f"Keys: {keys1}")
            return keys1
        except Exception as e:
            logging.exception(e)

    def value_elements(self):
        '''Prints key elements for every dictionary in the list'''
        try:
            val1 = []
            for i in self.l:
                if type(i) == dict:
                    val1.append(i.values())
            logging.info(f"Values: {val1}")
            return val1
        except Exception as e:
            logging.exception(e)

    def list_elements(self):
        '''Prints list elements in the list'''
        try:
            list1 = []
            for i in self.l:
                if type(i) == list:
                    list1.append(i)
            logging.info(f"List Elements: {list1}")
            return list1
        except Exception as e:
            logging.exception(e)

    def tuple_elements(self):
        '''Prints tuple elements in the list'''
        try:
            tuple1 = []
            for i in self.l:
                if type(i) == tuple:
                    tuple1.append(i)
            logging.info(f"Tuple Elements: {tuple1}")
            return tuple1
        except Exception as e:
            logging.exception(e)

    def num_elements(self):
        '''extract all the Numeric data it may be a part of dict key and values'''
        try:
            num = []
            for i in self.l:
                if type(i) == list:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == tuple:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == set:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == dict:
                    for j in list(i.keys()):  # extract keys as list
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                    for j in list(i.values()):  # extract values as list
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
            logging.info(f"Numeric Data: {num}")
            return num
        except Exception as e:
            logging.exception(e)

    def sum_num_elements(self):
        '''extract all the Numeric data it may be a part of dict key and values'''
        try:
            num = []
            for i in self.l:
                if type(i) == list:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == tuple:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == set:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == dict:
                    for j in list(i.keys()):  # extract keys as list
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                    for j in list(i.values()):  # extract values as list
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
            sum = 0
            for i in num:
                i = int(i)
                sum = sum + i
            logging.info(f"Sum of Numeric Elements: {sum}")
            return sum
        except Exception as e:
            logging.exception(e)

    def odd_elements(self):
        '''Prints odd numbers in the list'''
        try:
            num = []
            for i in self.l:
                if type(i) == list:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == tuple:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == set:
                    for j in i:
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                if type(i) == dict:
                    for j in list(i.keys()):  # extract keys as list
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
                    for j in list(i.values()):  # extract values as list
                        j = str(j)
                        if j.isnumeric() == True:
                            num.append(j)
            odd = []
            for i in num:
                i = int(i)
                if i % 2 != 0:
                    odd.append(i)
            logging.info(f"Odd Elements: {odd}")
            return odd
        except Exception as e:
            logging.exception(e)

    def occurance(self):
        '''Prints frequency of all the data'''
        try:
            data = []
            for i in self.l:
                if type(i) == list:
                    for j in i:
                        j = str(j)
                        data.append(j)
                if type(i) == tuple:
                    for j in i:
                        j = str(j)
                        data.append(j)
                if type(i) == set:
                    for j in i:
                        j = str(j)
                        data.append(j)
                if type(i) == dict:
                    lst = list(i.keys())
                    for j in lst:
                        j = str(j)
                        data.append(j)
                    lst = list(i.values())
                    for j in lst:
                        j = str(j)
                        data.append(j)
            freq = {}
            for i in data:
                if i not in freq:
                    freq[i] = 1
                else:
                    freq[i] += 1
            logging.info(f"Occurance of each element: {freq}")
            return freq
        except Exception as e:
            logging.exception(e)

    def alphanum_data(self):
        '''Extracts Alpha Numeric Data'''
        try:
            alnum = []
            for i in self.l:
                if type(i) == int:
                    alnum.append(i)
                if type(i) == list:
                    for j in i:
                        j = str(j)
                        if j.isalnum() == True:
                            alnum.append(j)
                if type(i) == tuple:
                    for j in i:
                        j = str(j)
                        if j.isalnum() == True:
                            alnum.append(j)
                if type(i) == set:
                    for j in i:
                        j = str(j)
                        if j.isalnum() == True:
                            alnum.append(j)
                if type(i) == dict:
                    lst = list(i.keys())  # extract keys as list
                    for j in lst:
                        j = str(j)
                        if j.isalnum() == True:
                            alnum.append(j)
                    lst = list(i.values())  # extract values as list
                    for j in lst:
                        j = str(j)
                        if j.isalnum() == True:
                            alnum.append(j)
            logging.info(f"Alpha Numeric Data: {alnum}")
            return alnum
        except Exception as e:
            logging.exception(e)

    def unwrap_data(self):
        '''Unwraps all the collection inside the collection of the given list and creates a flat list'''
        try:
            data = []
            for i in l:
                if type(i) == int:
                    data.append(i)
                if type(i) == list:
                    for j in i:
                        data.append(j)
                if type(i) == tuple:
                    for j in i:
                        data.append(j)
                if type(i) == set:
                    for j in i:
                        data.append(j)
                if type(i) == dict:
                    lst = list(i.keys())  # extract keys as list
                    for j in lst:
                        data.append(j)
                    lst = list(i.values())  # extract values as list
                    for j in lst:
                        if type(i) == str:
                            data.append(i)
                        if type(i) == list:
                            for j in i:
                                data.append(j)
            data.append(j)
            logging.info(f"Unwrapped Collection as a List: {data}")
            return data
        except Exception as e:
            logging.exception(e)


l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
     {"key1": "sudh", 234: [23, 45, 656]}]

list_object = list1(l)

list_object.reverse_list()
list_object.key_elements()
list_object.value_elements()
list_object.list_elements()
list_object.tuple_elements()
list_object.num_elements()
list_object.sum_num_elements()
list_object.odd_elements()
list_object.occurance()
list_object.alphanum_data()
list_object.unwrap_data()