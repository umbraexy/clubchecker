#!/usr/bin/python3

def clubcheck(money,age):
    if money >=10 and age <=18:
        delay()
        print("Oh boy...\nYou got some money there but you are not old enough.\n Go play with the other kids.")
    elif money<=10 and age >=18:
        delay()
        print("Yeah, you are old enough, but you ain't got no chips. \nCome back here when you get some.")
    elif money >=10 and age>=18:
        delay()
        print("Sheesh. You meet all the criteria. Come in.")
    else:
        delay()
        print("Oh hoh. You are too young to be here.\n You don't have any money either! \n Get out of here.")

def get_info(input):
    global rawmoney,rawage
    print("Welcome to the Inn's Club.")
    delay()
    rawmoney=(input("...How much money you got?\n"))
    delay()
    rawage=(input("...And how old are you, anyway?\n"))

def int_info(rawmoney,rawage):
    global money,age
    money=(int(rawmoney))
    age=(int(rawage))


def delay():
    import time
    time.sleep(1.4)

def pause():
    print('...')
get_info(input)

pause()


try:
    int_info(rawmoney,rawage)

except:
    delay()
    print("I am asking for numbers buddy... ")
    delay()
    print("Not letters.")
    delay()
    print("...Are you this dense?")
    delay()
    while (not(rawmoney.isnumeric())) or (not(rawage.isnumeric())):
        print("We are going to be here all day if you keep doing this. Try again.\n")
        delay()     
        get_info(input)
    else:
        int_info(rawmoney,rawage)
clubcheck(money,age)

