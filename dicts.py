import logging
logging.basicConfig(filename="dicts.log", level=logging.DEBUG)
logging.info("this is my dictionary log")
class dicts:
    def dict1(self, lists):
        logging.info("this function will extract dictionary from list")
        try:
            l1 = []
            for i in lists:
                if type(i) == dict:
                    l1.append(i)
                    logging.info(l1)
            return (l1)
        except Exception as e:
            logging.exception(e)

    def extractnum(self, lists):
        """This function will extract numerical values from the list even it is a dictionary"""
        global l1, l2
        logging.info("This function will extract numerical values from the list even it is a dictionary")
        try:
            l1 = []
            for i in lists:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                            logging.info(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
                                logging.info(g)
            l2 = []
            logging.info(l1)
            for i in lists:
                if type(i) == dict:
                    l2 = len(i)
            logging.info(l2)
            return l1, l2
        except Exception as e:
            logging.exception(e)
            logging.info("the output of numeric values are and number of keys in dictionary are", l1, l2)
list1=dicts()
print(list1.dict1([[1,2,3,4],(2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8}, ["ineuron", "data science "]]))
print(list1.extractnum([[1,2,3,4],(2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8}, ["ineuron", "data science "]]))
