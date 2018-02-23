# Written bu Uriel Kosayev

import random

# Encrypt
def encrypt(key):
    with open(r"answer-hidden.txt" ,'rb') as f:
        data = f.read()


    with open(r"answer.docx" , 'wb') as ans:
        pass



    for ch in data:
        with open(r"answer.docx" , 'ab') as ans:
            ans.write(chr(ord(ch) ^ key))


# Decrypt
def decrypt():

    key = random.randint(0,256)
    print "key : {}".format(key)
    with open(r"data_to_encrypt.docx" ,'rb') as f:
        data = f.read()


    with open(r"answer.txt" , 'wb') as ans:
        pass



    for ch in data:
        with open(r"answer-hidden.txt" , 'ab') as ans:
            ans.write(chr(ord(ch) ^ key))


