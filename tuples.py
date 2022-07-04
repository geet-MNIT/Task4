import logging
logging.basicConfig(filename="tuples.log", level=logging.DEBUG)
logging.info("this is my tuple log")
class tuples:
    """ this function is used to extract tuple from the list"""
    try:
        def tuple1(self, lists):
            l1=[]
            for i in lists:
                if type(i) == tuple:
                    l1.append(i)
            return l1
    except Exception as e:
        logging.exception(e)
list1=tuples()
print(list1.tuple1([[1,2,3,4],(2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8}, ["ineuron", "data science "]]))
