import logging
logging.basicConfig(filename="sets.log", level=logging.DEBUG)
logging.info("this is my set log")
class sets:
    def __init__(self, lists):
        logging.info('set Constructor is created')
        self.lists = lists

    def extract_set(self):
        try:
            logging.info('this function will extract set from list')
            l1 = []
            for i in self.lists:
                if type(i) == set:
                    l1.append(i)
            logging.info(l1)
            return l1
        except Exception as e:
            logging.error(e)
set1=sets([[1,2,3,4],(2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8}, ["ineuron", "data science "]])
print(set1.extract_set())
