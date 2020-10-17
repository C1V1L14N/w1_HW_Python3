# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, cash):
    list["admin"]["total_cash"] += cash

def get_pets_sold(list):
    return list["admin"]["pets_sold"]

def increase_pets_sold(list, cash):
    list["admin"]["pets_sold"] += cash
    
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
    for customer in customer_list:
        return customer_list["cash"]
    






    