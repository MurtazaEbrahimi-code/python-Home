# class user:
#     username = 'murtaza'
#     userlast = 'ebrahimi'
#     age = 19
#     def fullname(self):
#         return f'{self.username} {self.userlast}'
#     def __init__(self,username,userfamily):
#         self.username = username
#         self.userlast = userfamily
#
# murtaza = user('murtaza','ebrahimi')
# ali = user('ali','sajidi')
# print(ali.fullname())
# print(murtaza.fullname())
#
# -----------------------------------
#
# class car:
#     def __init__(self, carname, numdoors, color):
#         self.carname = carname
#         self.numdoors = numdoors
#         self.color = color
#
#     def info(self):
#         return f'car name is {self.carname} the door num is {self.numdoors} color is {self.color}'
#
#
# t = car('t',3,'red')
# print(t.info())
#
# li = [1, 34, 5, 3]
# l1 = ['murtza', 'ali']
# l1.extend(li)
# print(l1)
#
#
# l = [1, 3, 4, 5, 6]
# del l
# print(l)
#
# l = [1, 3, 4, 5, 6]
# del l[1]
# print(l)
#
# l = ['murtaza', 'ali', 'reza', 'akbar']
# for i in range(len(l)):
#     print(l[i])
# ------------------------------------------
#
# class user:
#
#     def __init__(self,username='unknow',userlast='unknow',userage=0,useremail='unknow'):
#         self.name = username
#         self.lastname = userlast
#         self.age = userage
#         self.email = useremail
#
#     def bay(self):
#         return f"{self.name} 'can boy all course'"
#
#     def read(self):
#         return f"{self.name} 'can read all course'"
#
#     def birthday(self):
#         return 2024 - self.age
#
# ali = user('ali','rezai',19,'ali99.gmail.com')
# murtaza = user()
# # print(ali.name,ali.lastname,ali.age,ali.email)
# # print(murtaza.name,murtaza.lastname,murtaza.age,murtaza.email)
# print(ali.read())
# print(ali.birthday())
# print(ali.bay())
#
# -name
# --name
# --name--
# ------------------------------------------
#
# class user:
#     def __init__(self,username, email):
#         self.name = username
#         self.email = email
#         self._pas = '444'
#         self.__message = 'i love py'
#
#     def login(self,password):
#         if self._pas == password:
#             print('login')
#
#         else:
#             print('not login')
#
# # murtaza = user('murtza','murtazaebrahimi21@gmail.com')
# # print(murtaza.name, murtaza._email)
# ali = user('ali','ali.com')
# # print(ali.name)
# # ali.login('444')
#
# print(ali._user__message)
# print(dir(ali))
# ------------------------------------------
#
# class user:
#     def __init__(self,username,userlast,userage):
#         self.name = username
#         self.last = userlast
#         self.age = userage
#
#
#     def fullname(self):
#         return f'{self.name} {self.last} {self.age}'
#
#     def adult(self):
#         return 'not adult'if self.age < 18 else 'adult'
#
# murtaza = user('murtaza','ebrahimi',19)
# # print(murtaza.fullname())
# # print(murtaza.adult())
#
# from test1 import culc
# cu = culc()
# print(cu.sum(1,2))
# print(cu.manfi(1,2))
# print(cu.multi(1,2))
# print(cu.divison(1,2))
# ------------------------------------------
#
# class user():
#     activeuser = 0
#     alowuser = ['murtaza','ali','ahmad']
#     loginuser = []
#     def __init__(self,getname,getfamily):
#         if getname not in user.alowuser:
#             raise ValueError(f'{getname} can not login')
#         self.name = getname
#         self.family = getfamily
#         user.activeuser += 1
#         user.loginuser.append(getname)
#         print(f'{self.name} he is logged in')
#
#     def logout(self):
#         print(f'{self.name} has log out')
#         user.activeuser -= 1
#         user.loginuser.remove(self.name)
#
# me = user('murtaza','ebrahimi')
# print(user.loginuser)
#
# you= user('ali','asghari')
# print(user.loginuser)
#
# print(user.activeuser)
# me.logout()
# print(user.loginuser)
#
# print(user.activeuser)
# me = user('murtaza','ebrahimi')
# you= user('ali','asghari')
# # print(user.alowuser)
# user.alowuser = ['sama']
# # print(user.alowuser)
# # me.alowuser = ['shcor']
# print(me.alowuser)
# print(user.alowuser)
# ------------------------------------------
# class user:
#     useractive = 0
#     def __init__(self,name,family):
#         self.name = name
#         self.family = family
#         user.useractive += 1
#         print(f'{self.name} has login')
#     def logout(self):
#         user.useractive -= 1
#         print(f'{self.name} has logout')
#
#     @classmethod
#     def activeuser(cls):
#         print(f'there are {cls.useractive} active user')
#     @classmethod
#     def strin(cls,string):
#         data = string.split(',')
#         return cls(data[0],data[1])
#
#
# murtaza = user('murtaza','ebrahim')
# ali = user('ali','ebrahim')
# print(user.useractive)
# ali.logout()
# print(user.useractive)
# user.activeuser()
# ali.logout()
# user.activeuser()
# x = user.strin('murtaza,ebrahimi')
# print(x.name,x.family)
# ------------------------------------------
#
# class person:
#     useractive = 'love python'
#     def __init__(self,name,family):
#         self.name = name
#         self.family = family
#
#     def fullname(self):
#         return f'{self.name} {self.family}'
#
#     def show(self):
#         return person.useractive
# class user(person):
#     pass
# mur = user('murtaza','ebrahimi')
# # print(mur.name)
# # print(mur.family)
# # print(mur.fullname())
# # print(mur.useractive)
# print(mur.show())
# ------------------------------------------
# class person:
#     def __init__(self,name, family, age):
#         self.name = name
#         self.family = family
#         if age >= 0:
#             self._age = age
#         else:
#             self.age = 0
#
#     def getAge(self):
#         return self._age
#
#     def setAge(self,agevalue):
#         if agevalue >= 0:
#             self._age = agevalue
#         else:
#             ValueError('uoy can not give nigetive age')
#     @property
#     def age(self):
#         return self._age
#     @age.setter
#     def age(self,value):
#         if value >= 0:
#             self._age = value
#         else:
#             ValueError('uoy can not give nigetive age')
#
# me = person('murtaza','ebrahimi',19)
# # print(me.age)
# # me.age = -11
# # me.setAge(-9)
# # print(me.setAge())
# print(me. age)
# me.age = -90
# print(me.age)
#
# ------------------------------------------
# class person:
#     def __init__(self,name, family):
#         self.name = name
#         self.family = family
#
#     @property
#     def fullname(self):
#         return f'{self.name} {self.family}'
#
# class user(person):
#     def __init__(self,name,family,email):
#         # person.__init__(self,name,family)
#         super().__init__(name,family)
#         self.email = email
#
# # me = user('murtaza','ebrahimi')
# me = user('murtaza','ebrahimi','murtaza@gmail.com')
# print(me.fullname)
# ------------------------------------------
# class person:
#     def __init__(self,name):
#         print('person init')
#         self.name = name
#
#     def sayhello(self):
#         return f'hello {self.name} in person class'
#
# class user:
#     def __init__(self,name):
#         print('user init')
#         self.name = name
#
#     def sayhello(self):
#         return f'hello {self.name} in user class'
#
#     def saybay(self):
#         return f'goodbay{self.name}'
# class admine(person,user):
#     def __init__(self,name):
#         print('admine init')
#         # super().__init__(name)
#         user.__init__(self,name)
#         person.__init__(self,name)
#
# me = admine('murtaza')
# print(me.saybay())
# # print(me.sayhello())
#
# class A:
#     def SayHello(self):
#         print('hello in A class')
# class B(A):
#     pass
#     # def SayHello(self):
#     #     print('hello in B class')
# class C(A):
#     pass
#     # def SayHello(self):
#     #     print('hello in C class')
# class D(B,C):
#     pass
#     # def SayHello(self):
#     #     print('hello in D class')
#
# itme = D()
# itme.SayHello()
# print(D.__mro__)
# print(help(D))
# class animal:
#     def makesound(self):
#         raise NotImplementedError
# ------------------------------------------
#
# class dog(animal):
#     def makesound(self):
#         return 'dog make sound'
#
#
# class cat(animal):
#     def makesound(self):
#         return 'cat make sound'
#
#
# animal1 = dog()
# animal2 = cat()
# print(animal1.makesound())
# print(animal2.makesound())
# ------------------------------------------
# class car:
#     def move(self):
#         raise NotImplementedError
#
#
# class benz:
#     def __init__(self, model):
#         self.model = model
#
#     def move(self):
#         print(f'{self.model} is moving')
#
#
# class corola:
#     def __init__(self, model):
#         self.model = model
#
#     def move(self):
#         print(f'{self.model} is moving')
#
#
# to = benz('langer')
# saracha = corola('saracha')
# print(to.move())
# print(saracha.move())
# ------------------------------------------
#
# class person:
#     def __init__(self, name, family, age):
#         self.name = name
#         self.family = family
#         self.age = age
#
#     def __len__(self):
#         return self.age
#
#     def __add__(self, other):
#         return self.age + other.age
#
#     def __mul__(self, other):
#         return self.age * other.age
#
#     def __truediv__(self, other):
#         return self.age / other.age
#
#     def
#
#
# person1 = person('murtaza', 'ebrahimi', 19)
# person2 = person('ali', 'safdari', 18)
# print(person1 + person2)
# print(person1 * person2)
# print(person1 / person2)
#
# # print(len(mur))
# ------------------------------------------
# number = (1, 4, 6, 8, 2, 10)
# name = 'murtaza'
# itername = iter(name)
# print(next(itername))
# print(next(itername))
# print(next(itername))
# print(next(itername))
#
#
# iternum = iter(number)
# print(next(iternum))
# print(next(iternum))
# print(next(iternum))
# print(next(iternum))
# print(next(iternum))
# print(next(iternum))
#
#
# for i in number:
#     print(i)
# ------------------------------------------
#
# def my_for(itrabl,func):
#     i = iter(itrabl)
#     while True:
#         try:
#             thing = next(i)
#         except StopIteration:
#             break
#         else:
#             squre(thing)
# def squre(number):
#     print(number ** 2)
#
# my_for([1, 2, 4, 5, 6, 7],squre)
# ------------------------------------------
#
# class counter:
#     def __init__(self, start, end, step = 1):
#         self.cur = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.cur < self.end:
#             num = self.cur
#             self.cur += self.step
#             return num
#         raise StopIteration
#
#
# number = counter(11, 19,2)
# iter(number)
# for i in number:
#     print(i)
# ------------------------------------------
#
# class user:
#     activeuser = []
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         userdict = {'name':name,'age':age}
#         user.activeuser.append(userdict)
#         self.index = 0
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index < len(user.activeuser):
#             person = user.activeuser[self.index]
#             self.index += 1
#             return person
#         raise StopIteration
#
# murtaza = user('murtaza',19)
# ali = user('ali',10)
# mustafa = user('mustafa',20)
# print(user.activeuser)
# for i in murtaza:
#     print(i)
# ------------------------------------------
# def count(num):
#     i = 0
#     while i < num:
#         yield i
#         i += 1
#
# counter = count(4)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# ------------------------------------------
# def fib(num):
#     li = []
#     a, b = 0, 1
#     while len(li) < num:
#         li.append(a)
#         a, b = b, a + b
#     return li
#
# print(fib(7))
#
# ------------------------------------------
# genrator = (num for num in range(10))
# print(genrator)
# print(next(genrator))
# ------------------------------------------
# def sum(num,func):
#     t = 0
#     for i in range(1, num + 1):
#        t += squer(i)
#     return t
# def squer(n):
#     return n * n
# print(sum(5,squer))
# ------------------------------------------
# from functools import wraps
#
#
# def my_decr(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print('bye boys')
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @my_decr
# def say_hello(name, family, age):
#     print(f'hello {name} {family} your age is {age}')
#
#
# print(say_hello.__name__)
#
# say_hello('murtaza','ebrahimi',19)
# x = my_decr(say_hello())
# x()
# ------------------------------------------
# from functools import wraps
# def is_allow(is_show):
#     def my_decr(func):
#         @wraps(func)
#         def inner():
#             if is_show:
#                 func()
#             else:
#                 print('your age shoud be up 18 to give vote')
#         return inner
#     return my_decr
#
#
# @is_allow(False)
# def can_you():
#     print('you can vote')
# can_you()
# ------------------------------------------
# def cheack(checkchar):
#     def my_decr(func):
#         def inner(name):
#             if len(name) > checkchar:
#                 print('error!!! is wrong')
#             else:
#                 func(name)
#             return func
#
#         return inner
#
#     return my_decr
#
# @cheack(8)
# def you_name(name):
#     print(name)
# you_name('murtaza ali')
# ------------------------------------------
# from time import time
# def my_decr(func):
#     def wrapper(*args, **kwargs):
#         star_time = time()
#         result = func(*args, **kwargs)
#         end_time = time()
#         print(end_time - star_time)
#         return result
#
#     return wrapper
#
# @my_decr
# def sum_num():
#     return sum(n for n in range(50000000))
#
# sum_num()
# --------------------------------------------------------

# class Car:
#     def __init__(self,model,price,color):
#         self.model = model
#         self.price = price
#         self.color = color

#     def __str__(self):
#         return f'car model {self.model} \ncar price {self.price}\ncar color {self.color}'

#     def __eq__(self, other):
#         return self.price == other.price

#     def __gt__(self, other):
#         return self.price > other.price

#     def __add__(self, other):
#         return self.price + other.price

# car1 =Car('taxi',4000,'red')
# car2 = Car('taxi',4000,'red')
# print(car1 + car2)

# --------------------------------------------------------
# class animal:
#     def __init__(self,type,color) -> None:
#         self.type = type
#         self.color = color
        
    
#     def eat(self):
#         print('eat')
        
#     def Go(self):
#         print('Go')

# class Bird(animal):
#     def __init__(self,type,color,wedght):
#         super().__init__(type,color)
#         self.wedght = wedght
#     def eat(self):
#         super().Go()
#         print('bird eat')

# b = Bird('bird','red',90)
# print(b.type)
# b.eat()

# --------------------------------------------------------

# def factorial(num):
#     if num == '0' or 0:
#         return 1
#
#     return num * factorial(num-1)
#
# print(factorial(9))

# --------------------------------------------------------





