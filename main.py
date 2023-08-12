
backpack = ("2 kg", "$10")

known_weight = 2
known_price = 10

selected = False
global_weight = 0 
global_price = 0

water_bottle = ("0.5 kg", "$0.2", 0.5, 0.2)
bread = ("0.68 kg", "$4", 0.68, 4)
jam = ("0.34 kg", "$5", 0.34, 5)
butter = ("0.25 kg", "$3", 0.25, 3)
cheese = ("0.4 kg", "$6", 0.4, 6)
milk = ("1 kg", "$2", 1, 2)
apple = ("0.2 kg", "$1", 0.2, 1)
banana = ("0.15 kg", "$0.5", 0.15, 0.5)
orange = ("0.3 kg", "$0.75", 0.3, 0.75)
egg_dozen = ("0.6 kg", "$1.5", 0.6, 1.5)
yogurt = ("0.15 kg", "$2", 0.15, 2)
carrot = ("0.25 kg", "$1", 0.25, 1)
lettuce = ("0.3 kg", "$1.5", 0.3, 1.5)
chicken_breast = ("0.4 kg", "$7", 0.4, 7)
rice_kg = ("1 kg", "$3", 1, 3)
pasta_kg = ("1 kg", "$2", 1, 2)
tomato = ("0.1 kg", "$0.5", 0.1, 0.5)

products = ["water_bottle",
"bread",
"jam",
"butter",
"cheese",
"milk",
"apple",
"banana",
"orange",
"egg_dozen",
"yogurt",
"carrot",
"lettuce",
"chicken_breast",
"rice_kg",
"pasta_kg",
"tomato"]

products_teg = [water_bottle,
bread,
jam,
butter,
cheese,
milk,
apple,
banana,
orange,
egg_dozen,
yogurt,
carrot,
lettuce,
chicken_breast,
rice_kg,
pasta_kg,
tomato]

# for i in range(len(products)):
#     print(products[i], products_teg[i], "-", i + 1)

run = True
run_2 = True

def output():
    print("You have backpack", backpack)
    print("And this item: ")
    for i in range(len(products)):
        print(products[i], products_teg[i], "-", i + 1)
    print("you need to pack everything you can fit in the backpack!")
    print("input number product (1, 17): " )

def comparison(index):
    global global_weight, global_price
    name = products[int(index) - 1]
    str_weight, str_price, int_weight, int_price = products_teg[int(index) - 1]

    global_weight += int_weight
    global_price += int_price
    
    b_weight = 2
    b_price = 10
    
    if global_weight < b_weight or b_price < int_price:
        print("Yeah, go ahead.")
        print(backpack[0], "/", global_weight, " kg", "\n"
              , backpack[1], "/", "$" , global_price )
    else:
        print("Oh this hight!")
        print(backpack[0], "/", global_weight, " kg", "\n"
              , backpack[1], "/", "$" , global_price )
    del products[index]
    del products_teg[index]
    
def input_product(select):
    global selected, run_2, run
    while run_2:
        if select.isdigit() and int(select) > 0:
            selected = True
            if selected:
                print("You selected")
                print(products[int(select) - 1], products_teg[int(select) - 1], "-", int(select))
                comparison(int(select) - 1)
        elif select == "stop":
            run = False
            run_2 = False
        select = input("Enter the next product number (or 'stop' to finish): ")

while run:
    output()
    input_product(input())