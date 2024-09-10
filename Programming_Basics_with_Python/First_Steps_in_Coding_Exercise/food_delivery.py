numbers_of_chicken_menu = int(input())
numbers_of_fish_menu = int(input())
number_of_vegan_menu = int(input())

chicken_menu_price = numbers_of_chicken_menu * 10.35
fish_menu_price = numbers_of_fish_menu * 12.40
vegan_menu_price = number_of_vegan_menu * 8.15
total_menus_price = chicken_menu_price + fish_menu_price + vegan_menu_price
desert_price = total_menus_price * 0.2
delivery_price = float(2.50)
total_price = total_menus_price + desert_price + delivery_price

print(total_price)