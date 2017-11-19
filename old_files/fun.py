'''''
измени алгоритм так, чтобы внути цикла рисовалось все правильно
'''
import os
import sys
import random as r


def forest(amount):
    foresthigh = [r.randrange(2,15) for i in range(amount)]
    myforest = ["" for i in range(amount)]


    for i in range(0,max(foresthigh)):
        branch = 1
        for j in range(amount):
            f = foresthigh[j] - i
            v = (f * ' ', '#' * branch)
            myforest[j] += ''.join(v)
        branch += 2
        #myforest += v * " " +  "#"
    #myforest = str(myforest)

  #  print(myforest, sep='\n')
    for i in myforest:
        print(i)

def test():
    l1 = ["1" for i in range(10)]
    l2 = ["2" for i in range(10)]
    l1.extend(l2)
    for i in l1:
        print(i)

amount = r.randrange(2,5)
print("lets create a forest with {} trees ".format(amount))
forest(amount)
#test()