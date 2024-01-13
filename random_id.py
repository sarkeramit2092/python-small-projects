import random
import time

new_id = []

def intro ():
    print ("Generate ID")
    generate_name()

def generate_name():
    names = ["amit", "anik", "shuvo", "joyti"]
    x = random.choice(names)
    print("Generating random name.....")
    time.sleep(1)
    print(x)
    new_id.append(x)
    surname()

def surname():
    surenames = ["sarker", "roy", "halder", "sarker"]
    x = random.choice (surenames)
    print ("Generating random surrname....")
    time.sleep(2)
    print(x)
    new_id.append(x)
    countryname()

def countryname():
    countries = ["bd", "denmark", "usa", "norway"]
    x = random.choice (countries)
    print ("Generating random country name....")
    time.sleep(3)
    print(x)
    new_id.append(x)
    my_new_id()

def my_new_id():
    print ("Your new ID is: ")
    print (new_id)

intro ()

