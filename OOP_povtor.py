"""ООП - Объектно - ориентированное программирование (парадигма)"""

""" 
    Принципы ООП:
    "Основные"
    1. - Наслдеование
      1.2 - Множественное наследование
    2. - Полиморфизм
    3. - Инкапсуляция
    "Дополнительные"
    # 1. - Абстракция
    # 2. - Ассоциация
      # 2.1 - Аггрегация
      # 2.2 - Композиция
"""


"""
Наследование - принцип ООП, где мы можем 
в доч.классе унаследовать, переопределять и использовать все методы и аттр род.класса

"""
from inspect import Attribute


class A:
    def method1(self):
        """Этот метод выводит строку"""
        print("method1 in class A")

class B(A):
    """Наследовали все методы и аттр у класса А"""

b = B() #Создали обьект(экземпляр) от класса В
b.method1() #Можем вызвать метод , который был создан в классе А

"""
Полиморфизм - принцип ООП, где мы можем создавать в разных классах 
одноименные методы и аттр с разным функционалом

"""

class A: 
    def __str__(self) -> str:
        """
        метод __str__ работает когда:
        1. мы оборачиваем обьект в str -> str(A())
        1. принтим обьект -> print(A)

        """
        return "A object"

class B:
    def __str__(self) -> str:
        return "B object"

print(A()) # A object
print(B()) # B object


"""
Инкапсуляция - принцип ООП, где мы можем делать 
аттр и методы  с разным уровнем доступа

"""
class A:
    attribute1 = "публичный аттрибут"
    _attribute2 = "защищенный аттрибут"
    __attribute3 = "приватный аттрибут (но можно обратиться так: _A__attribute3)"

    def method1(self):
        return "публичный метод"
    def _method2(self):
        return "защищенный метод"
    def __method3(self):
        return "приватный метод (_A__method3)"
    
"""
Множественное наследование - принцип ООП, 
в котором мы наследуем все аттр и методы у всех родителей

"""

class A:
    def method_a(self):
        pass
class B:
    def method_b(self):
        pass
class C(A, B):
    """
    Класс унаследовал все аттр и методы от класса А и В
    и все аттр и методы их родителей(object)
    
    """
c = C()
c.method_a()
c.method_b()

"""Проблемы множественного наследования"""
# 1. - Проблема ромба (решена через mro)
# 2. - Проблема перекрестного наследования (не решена)


# Проблема ромба
class A: 
    """корневой класс"""
    def method_a(self):
        return "A" 

class B(A):
    """первый доч.класс"""
    def method_b(self):
        return "B"

class C(A):
    """второй доч.класс"""
    def method_c(self):
        return "C"

class D(B,C):
    """дочерний класс от В и С"""
    def method_d(self):
        return "D"

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()

# проблема перекрестного наследования

class A:
    pass

class B:
    pass

class C(A, B):
    pass

class D(B, A):
    pass

class E(C, D):
    pass


"""Getters and Setters"""
# это методы, через которые мы можем получать (getter)
# и изменять (setter) значения защищенных и приватных аттрибутов

class A:
    _attr1 = "защищенный аттр"
    __attr2 = "приватный аттр"

    def get_attr1(self):
        return self._attr1
    
    def get_attr2(self):
        return self.__attr2

    def set_attr1(self, value):
        self._attr1 = value
        
    def set_attr2(self, value):
        self.__attr2 = value

a = A()
print(a.get_attr1, a.get_attr2)
a.set_attr1("NEW!")
a.set_attr2("VAL!")
print(a.set_attr1, a.set_attr2)
