class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

#Shows the object's address in memory
iphone = Phone("Iphone 7+", 300)
samsung = Phone("Samsung S20", 1400)

#Prints String representation of the object
print(iphone.brand)
print(iphone.price)
iphone.call("999")

print(samsung)
print(iphone)