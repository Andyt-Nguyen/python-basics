#Functions

def sayHello(name):
    hi = 'Hi there, ' + name
    return hi

jim = sayHello('Jim')
print(jim)

def addOneToNum(num):
    num = num + 1
    print('Num inside function', num)
    return

#Numbers are immuntable
num = 5
addOneToNum(num)
print('Outside of num function', num)

def addToList(list):
    list.append(4)
    print('List inside of func', list)
    return

list = [1,2,3]
addToList(list)
print('List outside of func', list)

