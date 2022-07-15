# iNeuron Blogs (Multi Layer Inheritance)
# User posts an article on blog.ineuron.ai
# post class inherits from blog class. Blog class inherits from Account_Class class (imported from UserInfo module)

import logging
logging.basicConfig(filename='Blog.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

from UserInfo import Account_Class

if __name__ == '__main__':
    class Blog(Account_Class):
        def __init__(self, title, category, description, text, *tags):
            """title of the Blog, Blog category, Blog description, Blog text, Blog tags"""
            self.title = title
            self.category = category
            self.description = description
            self.text = text
            self.tags = tags

    class Post(Blog):
        def preview(self):
            """shows preview of the article"""
            logging.info(f"This is a preview of your article on {self.title}: {self.text}. Click \"Submit\" to Post it")

        def submit(self):
            """submits the article for moderator approval"""
            logging.info(f"Your article on {self.title} has been submitted to moderator for approval")


    # user fills the compulsory fields to Post an article on the Blog

    article1 = Post("EDA", "Data Analytics", "EDA of Covid19", "Sample Text",
                    ["Covid19", "Python", "Data", "Visualization"])

    article1.login_check("test","passw33")  # Validate Login: user enters wrong userID

    article1.login_check("user55@gmail.com", "passw33")  # Validate Login: user enters correct user ID and password

    article1.preview()  # to preview the article before Posting on the Blog

    article1.submit()   # article1.submit()