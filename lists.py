import logging
logging.basicConfig(filename="lists.log", level=logging.DEBUG)
logging.info("this is a list log file")
class lists:
    def reverse(self,lists):
        try:
            """ this function is used to reverse a list"""
            logging.info("this is revere of the list")
            return lists[::-1]
        except Exception as e:
            logging.exception(e, "please enter a valid list")

    def extract(self, lists):
        """Extracts the given elements"""
        try:
            logging.info("The given list for this operation is %s", lists)
            return lists[7][0], list(lists[8].keys())[1], lists[5][1], lists[5:7], lists[8]['key1'], list(lists[8].values())
        except Exception as e:
            logging.exception(e)

    def extract_list(self, lists):
        """ this function will extract only list type"""
        try:
            l=[]
            for i in lists:
                if type(i) == list:
                    l.append(i)
            return l
        except Exception as e:
            logging.exception(e)

    def summ(self, lists):
        """ this function will calculate the sum of numeric data"""
        try:
            logging.info("the numeric values are generated")
            l1 = []
            for i in lists:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int:
                                l1.append(g)
            return l1, sum(l1)
            logging.info("the sum of numeric values is", sum(l1))
        except Exception as e:
            logging.exception(e, "please accept numeric values only")

    def odd_num(self, lists):
        """This will give odd numeric values from the list"""
        try:
            l2 = []
            for i in l1:
                if i%2==0:
                    pass
                else:
                    l2.append(i)
            return l2
            logging.info("The odd numeric values are %d", l2)
        except Exception as e:
            logging.exception(e)

    def extract_ineuron(self, lists):
        """ this function is used to extract ineuron from the list"""
        logging.info("Extract ineuron")
        try:
            l1=[]
            for i in lists:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                           l1.append(j)
                           logging.info(j)

                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == 'ineuron':
                               l1.append(g)
                               logging.info(g)
            return l1
        except Exception as e:
            logging.exception(e)
            logging.info("The string is extracted")

    def occur(self, lists):
        """ This function is created to check the occurence of each element"""
        logging.info("tell the occurence of element")
        try:
            l1 = []
            for i in lists:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l1.append(j)
                            logging.info(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l1.append(g)
                                logging.info(g)
            for i in set(l1):
                logging.info("The count is displayed")
                print(i, ":", l1.count(i))
        except Exception as e:
            logging.exception(e)

    def alphanum(self, lists):
        """ To check for alphanumeric """
        logging.info("to check whether the element is alphanum or not")
        try:
            l1 = []
            for i in lists:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int or type(j) == str:
                            l1.append(j)
                            logging.info(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                l1.append(g)
                                logging.info(g)
            l2 = []
            for i in l1:
                if type(i) == str:
                    if i.isalnum():
                       l2.append(i)
            return l2
        except Exception as e:
            logging.exception(e)

    def str_len(self, s) :
        """you have to write a fun which will take string and return a len of it without using a inbuilt fun len"""
        try:
            count = 0
            for i in s:
                count = count + 1
            return count
            logging.info(count)
        except Exception as e:
            logging.exception(e)

l=[[1,2,3,4],(2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {'k1' :"sudh" , "k2" : "ineuron","k3":
            "kumar" , 3:6 , 7:8}, ["ineuron", "data science "]]
list1= lists()
list2= lists()
print(list1.reverse([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]))
print(list1.extract([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]))
print(list2.extract_list(l))
print(list2.summ(l))
print(list2.extract_ineuron(l))
print(list2.occur(l))
print(list2.alphanum(l))
print(list2.str_len("gfhjgkhjkhgfcffhkjj"))
