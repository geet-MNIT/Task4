import logging
logging.basicConfig(filename="strings.log", level=logging.DEBUG)
logging.info("this is a string log file")
class my_string:
    def extract(self):
        """ This will extract the string"""
        logging.info("extract the string")
        try:
            s = input("enter the string")
            return s[0:300:3], s[::-1]
        except Exception as e:
            logging.exception(e)


    def split_string(self):
        """ This function is used to perform split, lower and capitalize operations on string"""
        try:
            logging.info("This function is used to perform split, lower and capitalize operations on string")
            s = input("enter the string")
            s1 = s.upper()
            return s1.split(), s.lower(), s.capitalize()
        except Exception as e:
            logging.exception(e)

    def expand(self):
        """ Expand tabs is used"""
        try:
            logging.info("This function is used to perform Expand tabs operation")
            s = input("enter the string")
            return s.expandtabs()
        except Exception as e:
            logging.exception(e)

    def strip(self):
        """ The strip, center and replace operation is performed here"""
        try:
            logging.info("The strip, center and replace operation is performed here")
            s = input("enter the string")
            logging.info("the result is of strip, lstrip, rstrip, replace and cengter are stored in:", s.strip(), s.lstrip(), s.rstrip(), s.replace("my", "yours"), s.center(10, "*"))
            return s.strip(), s.lstrip(), s.rstrip(), s.replace("my", "yours"), s.center(10, "*")
        except Exception as e:
            logging.exception(e)

string1=my_string()
print(string1.extract())
print(string1.split_string())
print(string1.expand())
print(string1.strip())



