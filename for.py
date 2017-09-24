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

for f in studentF:
    for l in studentL:
        f + l
        print(f + l)


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
'''
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
