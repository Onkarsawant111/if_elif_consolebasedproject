
automobile = input("what are you looking for: ")
if automobile == "Bike":
    company = input("Which Company: ")
    if company == "Bajaj":
        bike = input("which bike: ")
        if bike == "Splender":
            print('Model name: 001, bikename: Splender, Price: 85,000rs')
        if bike == "Pulser220":
            print('Model name: 002, bikename: Pulser 220, Price: 1,15,000rs')
    if company == "Yamaha":
        bike = input("bike: ")
        if bike == "Frazer":
            print('Model name: 001, bikename: Frazer, Price: 95,000rs')
        if bike == "Zmr":
            print('Model name: 002, bikename: ZMR, Price: 1,25,000rs')
elif automobile =="Car":
    company = input("Which company you are looking for: ")
    if company == "Maruti Suzuki":
        car = input("Car: ")
        if car == "Swift":
            print('Model name: 001, carname: swift, Price: 6,85,000rs')
        if car == "Alto800":
            print('Model name: 002, carname: Alto, Price: 3,15,000rs')
    if company == "Tata":
        car = input("car: ")
        if car == "Harrier":
            print('Model name: 001, carname: Harrier, Price: 9,95,000rs')
        if car == "Safari":
            print('Model name: 002, carname: Safari, Price: 11,25,000rs')
elif automobile == "Accessories":
    parts = input("which parts you are looking for:")
    if parts == "Headlights":
            print("Price:2000rs")
    if parts == "Seat":
            print("price:5000rs")
else:
        print("Oops! The product you are looking for is not available")
    
    