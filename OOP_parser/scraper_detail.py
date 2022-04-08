class A():
    def __init__(self, a, b) -> None:
        self.a = a 
        self.b = b
        print(self.a, self.b)

class B(A):
    pass

b = B(12, 14)