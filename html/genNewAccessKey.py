import os
import time
import random
import string

def genRandomKey(length):
    letters = string.ascii_lowercase + string.ascii_uppercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

key = genRandomKey(128)


print('The current URL is: http://localhost/?c=' + key)
text_file = open("../key.txt", "w")
n = text_file.write(key)
text_file.close()


