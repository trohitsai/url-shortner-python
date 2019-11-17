import string 
import random 

class config(object):

    def generate_random_string(self):
        res =  ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(10))
        return ''.join(random.sample(res,len(res)))


    

    

