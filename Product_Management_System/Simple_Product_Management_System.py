
product_names=[]
product_is_bought=[]
product_price=[]


def help():
    help_text="""
        tasks:
        _add:add a new
        _remove:remove a product
        _edit:edits a product
        _search:search product
        _display:display product
        _buy:buy a pruduct
        _help:display help text
        _exit:exist the program
        _ditails:ditail product
        """
    print(help_text)


def add(name):
    if name not in product_names:
        product_names.append(name)
        product_is_bought.append(False)
        product_price.append(None)
        print("add")
    else:
        print(f"{name}already exist")


def display():
    if len(product_names)== 0:
        print("empty!")
    for i,p in enumerate(product_names):
        bought=product_is_bought[i]
        price=product_price[i]
        print(f"{i+1}) {p} ==> bought: {bought}, price: {price}")


def remove(name):
    if name in product_names:
        ind =product_names.index(name)
        print(ind)
        product_names.remove(name)
    product_names.pop(ind)
    product_price.pop(ind)
    product_is_bought.pop(name)


def edit(name):
    if old_name in product_names:
        new_name=input("new name:")
        if new_name not in product_names:
            ind=product_names.index(old_name)
            product_names[ind]=new_name
            new_price=int(input("new price:"))
            if product_price[ind] !=None:

                product_price[ind]=new_price
            else:
                print("not purchased")
            print("edited")
        else:
            print(f"{new_name}: already exist")
    else:
        print(f"{old_name}: not found")


def search(name):
    if name in product_names:
        ind = product_names.index(name)
        bought=product_is_bought[ind]
        price=product_price[ind]
        print(f"{name} ==> bought: {bought}, price: {price}")
    else:
        print(f"{name}:not found")


def ditail():
    total=len(product_names)
    not_purchased = product_is_bought.count(False)
    purchesed = product_is_bought.count(True)
    print(f"total:{total}")
    print(f"purchesed:{purchesed}")
    print(f"not purchased:{not_purchased}")
    prices=[]
    for i in product_price:
        if i:
            prices.append(i)
        print(f"sum:{sum(prices)}")


def buy(name):
    if name in product_names:
        price=int(input(f"price of {name}: "))
        ind=product_names.index(name)
        product_price[ind]=price
        product_is_bought[ind]=True
        print("bought")
    else:
        print(f"{name}: not found")


while True:
    answer=input("help,add,display,edit,remove,search,buy,ditails,exit:")

    if answer=="help":
        help()

    elif answer=="add":
        name=input("product name:")
        add(name)

    elif answer=="remove":
        name=input("product name:")
        remove(name)

    elif answer=="edit":
        old_name=input("product name:")
        edit(name)

    elif answer=="search":
        name=input("product name:")
        search(name)

    elif answer=="display":
        display()

    elif answer=="buy":
        name=input("product name:")
        buy(name)
        
    elif answer=="ditails":
        ditail()

    elif answer=="exit":
        break

    elif answer=="":
        continue

    else:
        print(f"{answer} comand not found")
