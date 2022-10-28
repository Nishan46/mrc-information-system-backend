import random
import string

def Get_token():
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(25))
     