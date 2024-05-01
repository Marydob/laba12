#12.1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Ресторан: ", self.restaurant_name)
        print("Тип кухни: ", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт!")
newRestaurant = Restaurant("Pappone", "Европейская кухня")
print("Название ресторана:", newRestaurant.restaurant_name)
print("Тип кухни:", newRestaurant.cuisine_type)
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
#11.2
res1 = Restaurant("Olivka", "Итальянская")
res2 = Restaurant("Geraldine", "Французская")
res3 = Restaurant("Sintoho", "Китайская")
res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()
class IceCreamStand(Restaurant):
    def __init__(self, name, flavors):
        super().__init__(name, "Ice Cream Stand")
        self.flavors = flavors

    def display_flavors(self):
        print("Доступные вкусы:")
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand("SWEETNEES", ["Ванильное", "Шоколадное", "Крем-брюле"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
#12.2
class IceCreamStand:
    def __init__(self, name, flavors, location, opening_hours):
        self.restaurant_name = name
        self.restaurant_type = "Ice Cream Stand"
        self.flavors = flavors
        self.location = location
        self.opening_hours = opening_hours

    def describe_restaurant(self):
        print("Restaurant:", self.restaurant_name)
        print("Type:", self.restaurant_type)

    def display_info(self):
        print("Ice Cream Stand:", self.restaurant_name)
        print("Location:", self.location)
        print("Opening Hours:", self.opening_hours)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"{flavor} добавили в меню")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"{flavor} удалено из меню")
        else:
            print(f"{flavor} отсутствует в меню")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"{flavor} есть в наличии")
        else:
            print(f"{flavor} нет в наличии")

    def serve_popsicle(self):
        print("в наличии мороженое на палочке")

    def serve_soft_serve(self):
        print("в наличии мягкое мороженое")

ice_cream_stand = IceCreamStand("SWEETNEES", ["Ванильное", "Шоколадное", "Крем-брюле"], "ул. Некрасова", "10:00-20:00")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_info()

ice_cream_stand.add_flavor("Клубничное")
ice_cream_stand.remove_flavor("Крем-брюле")
ice_cream_stand.check_flavor("Ванильное")

ice_cream_stand.serve_popsicle()
ice_cream_stand.serve_soft_serve()

#12.3

from PIL import Image, ImageDraw, ImageFont
image = Image.open('ice-cream.jpg')
draw = ImageDraw.Draw(image)
font2 = "System/Library/Fonts/Supplemental/Times New Roman.ttf"
font2 = ImageFont.truetype(font2, 24)
results = []
results.append("МЕНЮ SWEETNEES:")
results.append("    *  Ванильное")
results.append("    *  Шоколадное")
results.append("    *  Крем-брюле")
results.append("    *  Клубничное")
position = 370
for result in results:
    draw.text((390, position), result, font=font2, fill='brown')
    position += 30
image.save('ice-cream(new).png')
image.show()