class vehicle:
  def vehiclemake(self, make):
    self.vehiclemake = make
  def vehiclemodel(self, model):
    self.vehiclemodel = model

class car(vehicle):
  def cardoor(self, door):
    self.cardoor = door

class truck(vehicle):
  def trucklength(self, length):
    self.trucklength = length
  
def main():
  print("Please enter which of the following you would like to make:")
  response = input("Enter 1 to create a Car, Enter 2 to create a Truck. >")
  print("")
  match response:
    case "1":
      make_car()
    case "2":
      make_truck()
    case other:
      print("I'm sorry, that is not a valid option. Please try again.")
      print("")
      main()

def make_car():
  input_make = input("Please input the make of the car. (This is the brand, like Toyota or Honda.) >")
  input_model = input("Please input the model of the car. >")
  input_door = input("Please input how many doors this car has. >")
  print("")
  newVehicle = car()
  newVehicle.vehiclemake(input_make)
  newVehicle.vehiclemodel(input_model)
  newVehicle.cardoor(input_door)
  print(f"This car is a {newVehicle.vehiclemake} {newVehicle.vehiclemodel}, and has {newVehicle.cardoor} doors.")
  print("")
  print("This car has been added to your garage.")
  print("")
  main()

def make_truck():
  input_make = input("Please input the make of the truck. (This is the brand, like Toyota or Honda.) >")
  input_model = input("Please input the model of the truck. >")
  input_length = input("Please input the bed length of this truck, measured in feet. >")
  print("")
  newVehicle = truck()
  newVehicle.vehiclemake(input_make)
  newVehicle.vehiclemodel(input_model)
  newVehicle.trucklength(input_length)
  print(f"This truck is a {newVehicle.vehiclemake} {newVehicle.vehiclemodel}, and has a bed length of {newVehicle.trucklength} feet.")
  print("")
  print("This truck has been added to your garage.")
  print("")
  main()

main()