import os, time
from colorama import init, Fore, Back, Style
q = "    010101   0101010   "
w = "  101010101 010101010  " 
e = " 101010101010101010101 " 
r = "01010101010101010101010" 
t = "01010101010101010101010" 
y = " 010101010101010101010 " 
u = "  1010101010101010101  " 
i = "   01010101010101010   " 
o = "    101010101010101    " 
p = "      01010101010      " 
a = "        101010         " 
s = "         1010          " 

q = [ q , w , e , r , t ,y ,u ,i ,o ,p ,a, s]
w = q.copy()
init()

clear = lambda: os.system('cls')

def del_last(x) :
    x = x[:-1]
    return x

def disappearance(x):
    l_list = len(x)
    for i in range(l_list) :
        x[i] = del_last(x[i])
    return x


def gen_l(x):
    l = []
    while len(l) != len(x) :
        l.append("")
    return l

def anim1(x):
    clear()
    x = disappearance(x)
    for i in x :
        print(Fore.RED + i)

def appearance(x , y , z):
    for i in range(len(y)) :
        a = y[i]
        if x[i] != a :
            x[i] += a[z]
        else :
            pass
    return x

c = ["" , "" , ""]
v = ["123" , "234" , "345"]

def anim2(x , y , z):
    clear()
    x = appearance(x , y , z)
    for i in x:
        print(Fore.RED + i)
def f1(x):
    l = gen_l(x)
    if l != x :
        return True
    return False
def f2(x , y):
    if x != y :
        return True
    return False
def run1() :
    while f1(q):
        anim1(q)
        time.sleep(0.01)
def run2():
    p = -1
    while f2(q , w):
        p += 1 
        anim2(q , w , p)
        time.sleep(0.01)


while True:
    run1()
    run2()
