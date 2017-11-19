import random as r
import math
import  time as t
import os
from statistics import mean

def bubsort():
    randlist = [ r.randrange(0,100) for i in range(20)]
    print("befor sort",randlist)
    i = len(randlist) -1
    while i >1:
        j = 0
        while j<i:
            if randlist[j] > randlist[i]:
                temp = randlist[j]
                randlist[j] = randlist[i]
                randlist[i] = temp
            j+=1
        i-=1
    print("after sort ",randlist, end= ";")



def ex1():
    multlist = [[i]* 10 for i in range(10) ]

    print(str(multlist))



    for i in range(1,10):
        for j in range(1,10):
            multlist[i][j] = i * j

    print(str(multlist))

    mydirect = { 'name': 'Vova' , 'lname': 'Eremin'}

    print(mydirect)
    print("my name is", mydirect['name'])
    print(mydirect.keys(), mydirect.values())

    for i in mydirect.items():
        print(mydirect.get("name", "net"))

    mydirect.clear()
    mydirect['name'] = 'fff'
    print(mydirect.values())

#----

def ex2():
    employers = []
    item = {"name", "Lname"}


    while 1:
        req = input("Enter customer?")
        req = req.lower()
        if req == 'yes':
            item = input("Enter name and Last name: ").split()
            employers.append(item)
            print("Done!")
        elif req == "no":
            # print("{} : {}".format(employers.keys(),employers.values()))
            print(employers)
            break
        else:
            print("repeat please")


#----

def factorial1(num):
    if num <= 1:
        return 1
    else:
        return num * factorial1(num -1)


#---

def compfun():
    var = int(input("num?"))

    print("factorial: ",factorial1(var))
    print("exponent", int(math.exp(var)))
    print("pover 2 ", math.pow(2, var))

    def fibo(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibo(num-1) + fibo(num-2)


    print("first {} fibo:{} ".format(var, fibo(var)))


#---- os work


def file1():
    os.chdir("./output")
    print(os.getcwd())

    with open("myfile.txt", mode="w",encoding="utf-8") as File1:
        File1.write("blablabla\neshyo\niesho11111y")


    with open("myfile.txt", encoding="utf-8") as File1:
        linecoun = 1
        res = []
        while True:
            line = File1.readline()
            if not line:
                break
            else:
                res.append(line)
                print("{} line: {}".format(linecoun, res))
                linecoun += 1


def file2():
    os.chdir("./output")
    outl = {'linec': [], "line": [], "len": []}
    avr = 0
    with open("myfile.txt", encoding="utf-8") as File1:
        linec = 1
        while True:
            line = File1.readline()
            if not line:
                break
            else:
                outl['line'].append(line)
                outl['len'].append(len(line))
                outl['linec'].append(linec)
                linec+= 1
    avr = mean(outl['len'])
    return outl , avr

def printfile2(book):
    for key, item, len, avr in book.items():
        print("String {}: {} , len:{} , avr: {}".format(key,item,avr), end="")
    print("av len: {}".format(outl['avr']))

#printfile2(file2())
    def pr1r1():
    str , avr1 = file2()

    for i in str.items():
        print(i)
    print(avr1)


    tup1 = (3,4,3,2,5)
    tup2= tup1+ (3,3,5)
    print(tup2)

#---

