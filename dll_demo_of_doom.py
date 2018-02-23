# Written by Uriel Kosayev

import re

def ip(address):
    pattern = r'(?:\d{1,3}\.){3}\d{1,3}'
    if re.match(pattern, address):
        return True
    else:
        return False

def segment(address):
    segments = range(1,33)
    pattern = r'(?:\d{1,3}\.){3}\d{1,3}/'
    if re.match(pattern, address) and int(address.split(r'/')[1]) in segments:
        return True
    else:
        return False


def subnetmask(mask):
    pattern = r'(?:\d{1,3}\.){3}\d{1,3}/'
    if re.match(pattern, address) and int(address.split(r'/')[1]) in segments:
        return True
    else:
        return False

def mac(address):
    pattern  = r'[1-9A-F][1-9A-F]:[1-9A-F][1-9A-F]:[1-9A-F][1-9A-F]:[1-9A-F][1-9A-F]:[1-9A-F][1-9A-F]:[1-9A-F][1-9A-F]'
    if re.match(pattern, address):
        return True
    else:
        return False

def namefile(name):
    bl = ['/', '\\',':', '*', '?', '"', ">", "<", "|" ]
    pattern = r'.+\..+'
    for sign in bl:
        if sign in name:
            return False
    if re.match(pattern, name):
        return True
    else:
        return False

def mail(address):
	try:
		name = address.split("@")[0]
		domain = address.split("@")[1]
	except:
		return False
    pattern_name = r'[A-Za-z1-9]+'
    if not re.match(pattern_name, name):
        return False
    return True

def toint(string):
    try:
        string = int(string)
        return True
    except:
        return False
		

def url(address):
    pattern = r'https?://.+'
    if re.match(pattern, address):
        return True
    else:
        return False

if __name__=="__main__":
    pass

	
def landscn(name):
    pattern = r'ns[1-9]{7}.land.scn'
    if re.match(pattern, name):
        return True
    else:
        return False
