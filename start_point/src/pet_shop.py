# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, cash):
    list["admin"]["total_cash"] += cash

def get_pets_sold(list):
    return list["admin"]["pets_sold"]

def increase_pets_sold(list, num_pets):
    list["admin"]["pets_sold"] += num_pets
    
def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, type):
    breed_list = []
    for pet in shop["pets"]:
        if pet["breed"] == type:
            breed_list.append(pet["breed"])
    return breed_list

def find_pet_by_name(shop, pet_name):
    for name in shop["pets"]:
        if name["name"] == pet_name:
            return name

def remove_pet_by_name(shop, pet_to_remove):
    for pet in shop["pets"]:
        if pet["name"] == pet_to_remove:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer_list):
    return customer_list["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    
def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

#LANDMARK MOMENT! I GOT THIS FAR!

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(shop, pet, customer):
     if customer_can_afford_pet(customer, pet) == True:
         add_pet_to_customer(customer, pet)
         remove_pet_by_name(shop, pet)
         increase_pets_sold(shop, 1)
         remove_customer_cash(customer, pet["price"])
         add_or_remove_cash(shop, pet["price"])









    
    






    