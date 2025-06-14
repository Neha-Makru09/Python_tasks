d={"Boss": "Neha", "Player" : "Horse", "Manager" : "Raja", "Employee": "Tinku", "Peon": "Minu"} 
print(d)
for keys in d: 
    print(keys,d[keys])
    
print("\n\n\nCar rental Mini something")
    
car_rental={"Audi": 19000, "Mercedes": 23000, "Mitsubishi": 13000, "Swift": 8900, "Sunny": 18900, "Nano":9000}

base_price=10000 

print("We have the following cars in our rental area")
for keys in car_rental: print (keys)
choice=input("Enter the car that you wish to rent out: ").strip().title()

if choice in car_rental.keys(): 
    print("Yes, it is available.")
    price=base_price+car_rental[choice]
    print("That would cost you around: ", price, " INR only.")
    
else: 
    print("Sorry, the model is not available at the moment.")
