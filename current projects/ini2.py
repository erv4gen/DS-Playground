from inh import sum
import math
from  random import *

int1 = [1,21,21,3]
def sep():
    print("_______________________")


print(sum.getsum(1,2,3,4))

def mult_by(fun,num):
    return fun(num)

print(mult_by(math.sqrt,2))


def outffinc(num):
    def infunct(val):
        return val * num
    return infunct

dfunct = outffinc(10)

print(dfunct(2))

listoffunct = [mult_by,dfunct]

print(listoffunct[0](math.sin,2), listoffunct[1](4))

def isodd(list):
    return all( i % 2 != 0 for i in list)

def initf():
    def chechodd(fun, listf):
        return fun(listf)
    return chechodd
sep()
exf = initf()
print(exf(isodd,int1))



def newf(name:str,lname:str, age:int) -> str:
    print(name,lname,age)


newf("vlva","er",12)
print(newf.__annotations__)

#------

sum = lambda x,y : x+y

print(sum(4,4))


canvote = lambda x: True if x>18 else False

print(canvote(11))


poverlist = [
    lambda x: x**2,
    lambda x: x**3,
    lambda x: x**4]

for fun in poverlist:
    print(fun(2))

#-----

listattack = {'attack': ( lambda:print(' normal attach')),
              'missed': (lambda: print('missed attach')),
              'power': (lambda: print('power attack'))}

for i in range(10):
    tattack = choice(list(listattack.keys()))
    listattack[tattack]()

ins = ["head", "tail"]

listr = [choice(ins) for i in range(0, randrange(10,200))]
print("init list:",listr)
print("heads:", listr.count("head"))
print("tails:", listr.count("tail"))

toten = range(10)

print(list(map((lambda x: x**2),
          toten)))

aLinst = list(map( (lambda x , y : x+y),
                   [1,3,4,3,5,6,4,3],
                   [1, 3, 4, 3, 5, 6, 4, 3]))

print(aLinst)

#---
print(list(filter((lambda x : x%2 ==0),
                   range(10,100))))

#-----
print("cheack1")
initlist = [ randrange(1000) for i in range(100)]
exitlist = list(map( (lambda x : x*9),
                     initlist))

print('/9:', list(filter((lambda x: x % 9 == 0), exitlist)))

from functools import reduce

print(reduce((lambda x , y : "init {} , exit {}".format(x,y)),
    initlist,
    exitlist))


#----
l2 = [2,3,4,5,2]
l2= iter(l2)
for i in range(3):
    print(next(l2))

#---


class fibgenerator:
    def __init__(self,lim1):
        self.__lim = lim1
        self.__count = 0
        self.__sum = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.__count == self.__lim:
            raise StopIteration
        else:
            self.__count += 1
            self.__sum += (self.__count -1)
            return  self.__sum


fibo1 = fibgenerator(5)


sep()
for i in fibo1:
    print(i)


sep()


class fiboc2:
    def __init__(self):
        self.__first = 0
        self.__secont = 1

    def __iter__(self):
        return self
    def __next__(self):
       fiboitem = self.__first + self.__secont
       self.__first = self.__secont
       self.__secont = fiboitem
       return  fiboitem

fi = fiboc2()

for i in range(10):
    print(next(fi))

sep()

print([ x for x in [randrange(1000) for y in range(50)] if x % 9 == 0])



sep()

