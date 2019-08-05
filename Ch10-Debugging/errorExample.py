#! python3 
# Ch.10 Debuging - errorExample.py (pg. 217)

def spam():
    bacon()
def bacon():
    raise Exception('This is and error message')

spam()