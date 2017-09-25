'''
# practice if statement
age = 3

if age is 60:
	print('yo man')
elif age is 70:
	print('dude u old')
else:
	print('welp you are very old')


# list that combines multiple combinations of surnames
studentF = ['mike', 'dan', 'lucy', 'carmen']
studentL = ['storm', 'apple', 'green', 'lan']
names = zip(studentF, studentL)
for a, b in names:
    print(a, b)

# defined incrementation for loop
for x in range(5, 10, 4):
    print(x)


# magic number exercise
test = 6
for n in range(100):
    if n is test:
        print(n, 'magic number')
        break
    else:
        print(n)


# finding numbers that have 0 remainders
for x in range(100):
    if x % 4 == 0:
        print("remainder is 0", x)


# continue
numbers = [2, 6, 14, 12, 3, 10]
print("available numbers")
for x in range(1, 15):
    if x in numbers:
        continue
    print(x)


# functions test


def test(btc):
    amount = btc * 3091
    print(amount)
    return(amount)


test(4)
a = test(5)



def py(hello='Unknown'):
    if hello is '1':
        hello = '100'
    elif hello is '0':
        hello = '000'
    print(hello)


py('1')

a = 6000


def test2():
    print(a)
    a1 = 600
    print(a1)


def test():
    print(a)


test2()
test()

# keyword arguments
def test(name='mike', action="worked", item="spade"):
    print(name, action, item)


test()
test("may","bought",'club')
test(action="bought")

def test(*args):
    total = 0
    for x in args:
        total += x
    print(total)


test()
test(50, 60, 70)

# testing with sets(sets dont print duplicates)
food = {'banana', 'cereal', 'coke', 'beer', 'stuff', 'beer'}
print(food)

if 'banana' in food:
	print('you already have banana')
else:
	print('you need banana')

# Dictionary
classmates = {'dan': 'is a dude', 'laura': 'is a dudette', 'lucy': 'shes a meh'}
print(classmates)
print(classmates['lucy'])

for i, j in classmates.items():
    print(i + " " + j)

# modules
import random
x = random.randrange(1, 1000)
print(x)

# downloading an image
import random
import urllib.request
def download(url):
	name = random.randrange(1, 1000)
	fullname = str(name) + ".jpg"
	urllib.request.urlretrieve(url, fullname)

download('http://dfp3r41v9wmfi.cloudfront.net/wp-content/uploads/Emperor_penguins.jpg')

#making and reading files
filew = open('test.txt', 'w')
filew.write('testing the write\n things')
filew.close()

fr = open('test.txt', 'r')
text = fr.read()
print(text)

from urllib import request

url = 'http://samplecsvs.s3.amazonaws.com/SalesJan2009.csv'


def download(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest = r'goog.csv'
    fx = open(dest, 'w')
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download(url)

# web crawler
import requests
from bs4 import BeautifulSoup


def trade(maxpages):
    page = 1
    while page <= maxpages:
        url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
        source = request.get(url)
        plain_text = source.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findall('a', {'class': 'item-name'}):
            href = 'https://buckysroom.org/' + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1


trade()

#try/except/finally
while True:
    try:
        user = int(input("insert number \n"))
        print(user)
        break
    except ValueError:
        print("yo fool enter a number")
    except: #not a good idea cuz you wont know what problems would occur
    	break
    finally:
    	print("complete")


class Test:
    book = 3

    def loan(self):
        print(' you loaned a book')
        self.book -= 1

    def checkbook(self):
        if self.book <= 0:
            print("no more books")
        else:
            print(str(self.book))


test1 = Test()
test1.loan()
test1.checkbook()



class Test:

    def __init__(self):
        print('testing')

    def test2(self):
        print('testing2')


tester = Test()
tester.test2()



class Bookcase():
    def __init__(self, x):
        self.amount = x

    def books(self):
        print(self.amount)


raamat = Bookcase(5)
raamat2 = Bookcase(20)

raamat.books()
raamat2.books()


class Girl:

    gender = 'female'

    def __init__(self, name):
        self.name = name


r = Girl('Rachel')
s = Girl('Stacey')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)


# inheritance
class Parent():

    def lastname(self):
        print('ln')


class Child(Parent):

    def firstn(self):
        print('fn')

    def lastname(self):
        print('ffn')


name = Child()
name.firstn()
name.lastname()

# multiple inheritance


class Figure():
    def move(self):
        print('the figure is moving')


class Item():
    def take(self):
        print('item in inventory')


class Figurewithitem(Figure, Item):
    pass  # need a line? but want it empty? use pass


f = Figurewithitem()
f.move()
f.take()

# threading

import threading


class Messenger(threading.Thread):
    def run(self):
        for _ in range(1000):  # _ if i dont care about the variable just wanna loop x times
            print(threading.currentThread().getName())


x = Messenger(name='Sending messages')
y = Messenger(name='Receive messages')
x.start()  # with threading you dont use x.run() but start
y.start()

##unpacking lists
date, item, price = ['December 24,2017', 'knife', 9.52]
print(date)

first = ['name1', 'name2', 'name3']
last = ['name11', 'name22', 'name33']

names = zip(first, last)
for a, b in names:
    print(a, b)

# lambda


def answer(x): return x * 7


print(answer(5))

example = {
    'name1': 400,
    'name2': 500,
    'name3': 35.4,
    'name4': 241,
    'name5': 11
}

print(sorted(zip(example.values(), example.keys()))) #min/max/sorted

# struct
from struct import *
# storing as bytes data
packed_data = pack('iif', 6, 19, 4.76)
print(packed_data)

print(calcsize('if'))


income = [20, 50, 60]


def profit(dollar):
    return dollar * 2


new_income = list(map(profit, income))
print(new_income)
'''

