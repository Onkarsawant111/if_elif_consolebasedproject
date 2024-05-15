vehicle = input("what are you looking for bike/car :  ")
data = {"bike":['honda','hero'],
        "car":['maruti-suzuki','tata'],
        "company":{'honda':['shine','unicorn'],
                   'hero':['splender','yuva'],
                   'maruti-suzuki':['swift','aura'],
                   'tata':['harrier','punch']
                   }}
model = {'shine':{'price':95000},
         'unicorn':{'price':120000}
         }
print(data[vehicle])
select_veh = input(f"which company {vehicle} you are looking for : ")
select_mod = input(f'which {select_veh} you are looking for : ')
print(data['company'][select_veh])

