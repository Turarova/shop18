#ООП - объект ориентированное программирование 

# print(dir(object))
# class Person:
#     legs = 2
#     arms = 2
#     eyes = 2
#     mouth = 1
    
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age

#     def walk(self, km):
#         print(f"{self.name} ходит {km} km")

# person1 = Person("Nastya")
# print(person1.walk(10))



# class Person:
#     def __init__(self, name, age,sex) -> None:
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.is_run = False
#         self.is_go = False
#         self.is_speak = False
#     def speak(self):
#         if self.age > 5:
#             self.is_speak = True
#         if self.is_speak:
#             print("I can speak")
#         else:
#             print("I can't speak")
#     def go(self):
#         if self.age > 5:
#             self.is_go = True
#         if self.is_go:
#             print("I can go")
#         else:
#             print("I can't go")
#     def run(self):
#         if self.age > 5:
#             self.is_run = True
#         if self.is_run:
#             print("I can run")
#         else:
#             print("I can't run")



# person1 = Person("Nastya", 18, 'female')
# person1.go()
# person1.run()
# person1.speak()




# class Students:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#         self.books = []
#         self.knowledge = 0
#         self.is_ready_to_work = False
#         self.language = {}


#     def read_book(self, book_title):
#         self.books.append(book_title)
#         self.__add_points(100)

#     def do_hw(self):
#         self.__add_points(10)

#     def do_real_world_pr(self):
#         self.__add_points(50)
        
#     def __add_points(self, point):
#         self.knowledge += point
#         if self.knowledge >= 500:
#             print("This student is ready to work")
#             self.is_ready_to_work = True

#     def learn_language(self, name_of_lang, number):
#         if number < 1 or number > 100:
#             raise Exception("Invalid number")
#         self.language[name_of_lang] = number


# st1 = Students("John", "Connor")
# print(f"Количество баллов у {st1.name}:", st1.knowledge)
# st1.read_book("Terminator")
# st1.do_hw()
# st1.do_real_world_pr()
# st1.learn_language("Py", 90)
# print(st1.language)
# print(f"Количество баллов у {st1.name}:", st1.knowledge)


# class Base_crud:
#     def __init__(self) -> None:
#         self.data = []
#         self.id_ = 1
    
#     def get(self, ident):
#         for num in self.data:
#             if num.get(ident):
#                 return num
#             else:
#                 return None

#     def create(self, data: dict):
#         self.data.append({self.id_: data})
#         self.id_ += 1

#     def update(self, ident, data: dict):
#         pass

#     def delete(self, ident):
#         for num in self.data:
#             if num[ident]:
#                 self.data.remove(num)

    
# class Book(Base_crud):
#     pass

# book = Book()
# print("Before:",book.data)
# book.create({'name': 'Py'})
# book.create({'name': 'Js'})
# print("After:", book.data)
# print(book.get(1))



# Наследование
# Инкапсуляция - приватные и публичные методы или атрибуты
# Инкапсуляция - объединение в единоцелое атрибутов и методов

# class A():
#     a = 12
#     def init(self):
#         self.hello = 'hello'

#     def set(self):
#         print('set')

# public static method
# private static method

# _ - защищенный
# __ - приватный

# class BaseTest:
#     def equal(self, a, b):
#         return a == b

# class Test(BaseTest):
#     pass

# test = Test()
# print(dir(test))


# Полиморфизм


# task 1
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def show_author(self):
#         print(f'Автор этой песни {self.author}')

#     def show_title(self):
#         print(f'Название этой песни {self.title}')

#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')

# song = Song("Happy", "Pharrell Williams", "2013")
# song.show_title()
# song.show_author()
# song.show_year()


# task 2
# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         area = self.pi * self.radius**2
#         return area

# circle = Circle(2)
# circle.color = "red"
# circle.get_area()

# task 3
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом') 
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

# task 4
# class Taxi:
#     cost = 70
#     cost_km = 12
#     def __init__(self, name):
#         self.name = name
#     def get_total_cost(self, km):
#         total_cost = self.cost_km * km + self.cost
#         return f'Такси {self.name}, стоимость поездки: {total_cost} сом'

# taxi1 = Taxi('Namba')
# taxi2 = Taxi('Yandex')
# taxi3 = Taxi('Jorgo')
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))

# task 5
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', +996707707707)
# contact.get_info()

# task 6
# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
#     def count_percent(self):
#         percent_ = self.salary * self.percent / 100
#         total_per = percent_ * self.experience
#         return total_per

# obj = Salary(10000, 10)
# print(obj.count_percent())


# task 7
# from datetime import datetime
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
#     def get_year(self):
#         date_ = int(datetime.now().year)
#         return f'выиграл {date_ - self.year} лет назад'

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())



# task 8
# class Password:
#     def __init__(self, password):
#         self.password = password
#     def validate(self):
#         if len(self.password) < 8 or len(self.password) > 15:
#             raise Exception('Password should be longer than 8, and less than 15')

#         check_num = list(filter(lambda x: x.isdigit(), self.password))
#         if  len(check_num) == 0:
#             raise Exception('Password should contain numbers too')

#         check_alpha = list(filter(lambda x: x.isalpha(), self.password))
#         if len(check_alpha) == 0:
#             raise Exception('Password should contain letters as well')

#         check_symbol = list(filter(lambda x: x in '@#&$%!~*', self.password))
#         if len(check_symbol) == 0:
#             raise Exception('Your password should have some symbols')

#         else:
#             return 'Ваш пароль сохранен.'
#     def __str__(self):
#         b = "*" * len(self.password)
#         return b

# password = Password('joe@12345')
# print(password.validate())
# print(password)


# task 9
# from functools import reduce
# class Math:
#     def __init__(self, value):
#         self.value = value
#     def get_factorial(self):
#         list_ = [x for x in range(1, self.value + 1)]
#         res = reduce(lambda x, y: x * y, list_)
#         return res
#     def get_sum(self):
#         iter_num = str(self.value)
#         res1 = reduce(lambda x, y: int(x) + int(y), iter_num)
#         return res1
#     def get_mul_table(self):
#         res2 = ''
#         list1 = list(range(1, 11))
#         for x in list1:
#             mult = self.value * x
#             res2 += f'{self.value} x {x} = {mult}\n'
#         return res2
    
# num = Math(11)
# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())




# dict_ = {4: "jdd", 1: "hjc", 3: "skds"}
# list_ = list(dict_.items())
# list_.sort()
# print(list_)

# task 10
# class ToDo:
#     instances = {}
#     def __init__(self, task):
#         self.task = task

#     def give_priority(self, priority):
#         self.instances[priority] = self.task

#     def list_of_tasks(self):
#         list_ = list(self.instances.items())
#         list_.sort()
#         return list_

# todo1 = ToDo('сходить в кино')
# todo2 = ToDo('сделать домашку')
# todo3 = ToDo('выгулять собаку')
# todo1.give_priority(3)
# todo2.give_priority(1)
# todo3.give_priority(2)
# print(todo3.list_of_tasks())


# НАСЛЕДОВАНИЕ
# TASK 2
# class A:
#     def method1(self):
#         print('Основной функционал')
# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

# TASK3
# class MyString(str):
#     def __init__(self,value):
#         self.value = value
    
#     def append(self, value1):
#         self.value += value1

#     def pop(self):
#         value1 = self.value
#         self.value = self.value[:-1]
#         return value1[-1]

#     def __str__(self):
#         return self.value

# example = MyString('String') 
# example.append('hello')
# print(example) 
# print(example.pop()) 
# print(example) 

# TASK 4
# class MyDict(dict):
#     def __init__(self, dict_):
#         self.dict_ = dict_
#     def get(self, k):
#         if k not in self.dict_.keys():
#             return super().get(k, 'Are you kidding?')
#         else:
#             return self.dict_.get(k)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))


# TASK 5
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
#     def display_student(self):
#         print(f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')

# obj_student = Student('Rick', 21, 'science')
# obj_student.display() 
# obj_student.display_student() 

# TASK 6
# class ContactList(list):
#     def __init__(self, list_):
#         self.list_ = list_
#     def search_by_name(self, name):
#         list1 = []
#         for x in self.list_:
#             if name in x:
#                 list1.append(x)
#         return list1

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))


# TASK 7
# class SmartPhones:
#     battery = 0
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory

#     def charge(self, num):
#         self.battery += num

#     def __str__(self):
#         return f'{self.name} {self.memory}'

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, str_):
#         return f"sending {str_} from {self.name} {self.memory}"

# import datetime
# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         time = datetime.datetime.now().time()
#         return time
    
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello'))
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 


# TASK 8
# class CustomError(Exception):
#     def __init__(self, text_error):
#         self.text_error = text_error
    
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str):
#     if str.isupper() == True:
#         return f'ВСЕ ОТЛИЧНО! {str}'
#     else:
#         raise capitals_error
# print(check_letters("HELLO")) 
# print(check_letters("hello"))



# ПОЛИМОРФИЗМ

# TASK1
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}
# list_ = []
# list_.append(a)
# list_.append(b)
# list_.append(c)
# for x in list_:
#     print(len(x))

# TASK2
# class Dog:
#     def voice(self):
#         print("Гав")

# class Cat:
#     def voice(self):
#         print("Мяу")

# barsik = Cat()
# rex = Dog()

# def to_pet(animal):
#     animal.voice()
# to_pet(barsik) 
# to_pet(rex) 

# TASK3
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return "“Привет, меня зовут Иван Петров”"
# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return "“Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор”"
# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return "“Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”"
    

# person = Person("Иван", "Петров")
# employee = Employee("Иван", "Петров","компания Рога и копыта", "директор")
# student = Student("Иван", "Петров", "КГТУ", "3 курс")

# def get_human_info(obj):
#     print(obj.get_info())
# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 


# TASK4
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
    
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         return 1/2 * self.base * self.height

# class Square(Shape):
#     def __init__(self, lenght):
#         self.lenght = lenght
#     def get_area(self):
#         return self.lenght**2

# from math import pi
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         return pi * self.radius**2

# triangle = Triangle(6, 3)
# square = Square(4)
# circle = Circle(5)
# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area())


# TASK5
# class OS:
#     def __init__(self, version):
#         self.version = version
# class Windows(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'
# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'

# win = Windows(12)
# mac = MacOS(12)
# lin = Linux(12)
# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))


# TASK6
# class Language:
#     def __init__(self, level, type):
#         self.level = level
#         self.type = type

# class Python(Language):
#     def write_function(self, func_name, arg):
#         return f"def {func_name}({arg}):"
#     def create_variable(self, var_name, value):
#         return f"{var_name} = {value.__repr__()}"
# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         a = "{     }"
#         return f"function {func_name}({arg}) {a};"
#     def create_variable(self, var_name, value):
#         return f"let {var_name} = {value.__repr__()};"



# py = Python('mid', 3)
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))
# js = JavaScript('mid', 4)
# print(js.write_function('validate', 'form'))
# print(js.create_variable('password', 'john@123'))


# TASK7
# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol
    
# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         res = self.rate * amount
#         return f"$ {amount} равен {res} сомам"

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         res = self.rate * amount
#         return f"€ {amount} равен {res} сомам"

# TASK8
# class Planet:
#     def __init__(self,orbit):
#         self.orbit = orbit
# class Mercury(Planet):
#     def __init__(self,orbit):
#         super().__init__(orbit)
#     def get_age(self,earth_age):
#         res = earth_age * 365 //self.orbit
#         return f'на Меркурии ваш возраст составляет {res} лет'
# class Venus(Planet):
#     def __init__(self,orbit):
#         super().__init__(orbit)
#     def get_age(self,earth_age):
#         res = earth_age * 365 /self.orbit * 365
#         return f'на Венере ваш возраст составляет {round(res)} дней'
# class Jupiter(Planet):
#     def __init__(self, orbit):
#         super().__init__(orbit)
#     def get_age(self,earth_age):
#         res = (earth_age * 365 //self.orbit)*(24*365)
#         return f'на Юпитере ваш возраст составляет {res} часов'
# merc = Mercury(88)
# print(merc.get_age(20))
# ven = Venus(225)
# print(ven.get_age(20))
# jup = Jupiter(12)
# print(jup.get_age(20))
    



# ИНКАПСУЛЯЦИЯ
# TASK3
# class Car:
#     def __init__(self):
#         self.__speed = 0
#     def set_speed(self, num):
#         self.__speed = num
#     def show_speed(self):
#         return self.__speed
# car1 = Car()
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 



# TASK4
# class Car:
#     def __init__(self):
#         self.__speed = 0
    
#     @property --> для геттеров
#     def speed(self):
#         return self.__speed
    
#     @speed.setter --> для сеттеров
#     def speed(self, num):
#         self.__speed = num


# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)