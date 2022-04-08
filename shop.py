

class Product:
    __id = 1

    def __init__(self, title, desc, price):
        self.id = Product.__id
        self.title = title
        self.desc = desc
        self.price = price
        Product.__id += 1


class Order:
    def error(self, user):
        if user.bill < user.cart.get("total_price"):
            print(f"Извините, {user.name} у вас недостаточно средств")
            print("Пополните баланс, либо уберите что-то из корзины")
            if input("Пополнить баланс? (да): ") == 'да':
                amount = int(input('Введите сумму: '))
                user.add_bill(amount)
        

    def __init__(self, user):
        while user.bill < user.cart.get("total_price"):
            self.error(user)
        user.bill -= user.cart.get("total_price")
        print(f"Ваш заказ едет по адресу {user.address}")
        user.show_cart()
        user.clear_cart()
        print(f"У вас осталось {user.bill} сом")




class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.bill = 0
        self.cart = {"total_price":0}

    def add_bill(self, amount):
        self.bill += amount
    
    def add_to_cart(self, *products):
        for product in products:
            self.cart[product.id] = {"title": product.title,
                                     "price": product.price}
            self.cart["total_price"] += product.price
    
    def remove_from_cart(self, *products):
        for product in products:
            try:
                self.cart.pop(product.id)
                self.cart["total_price"] -= product.price
            except:
                print(f"{product.title} в вашей корзине нет")
    
    def show_cart(self):
        from pprint import pprint
        print(f"-------------\n{self.name}")
        pprint(self.cart)
        print('--------------')

    def clear_cart(self):
        self.cart.clear()
        self.cart["total_price"] = 0


ice_cream1 = Product("Magnat", "very testy", 96)
ice_cream2 = Product("Smak", "s kunjutom", 15)
plov = Product("Plov", "Uzgenskii", 150)
salat = Product("Shakarap", "Tomato", 50)

Nurkamila = User("Nurkamila", "Alamedin 1")
Nurkamila.add_bill(1000)
Nurkamila.add_to_cart(ice_cream1, salat, plov)

Uluk = User("Uluk", "Tunguch")
Uluk.add_bill(150)
Uluk.add_to_cart(ice_cream2, plov)


# Nurkamila.show_cart()
# Uluk.show_cart()

Nurkamila.remove_from_cart(plov)
Nurkamila.show_cart()

uluk_order = Order(Uluk)
