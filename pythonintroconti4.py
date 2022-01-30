#while True:
#    try:
  #      x = int(input("Please enter a number : "))
    #    print("You have entered : " + str(x))
      #  break
   # except ValueError:
     #   print("You have not entered a valid number, Plase try again")
print("---------------------")
class Parent:
    firstName = "Jahanzeb"
    lastName = "Naeem"

    def parentDetails(this):
        print("From Parent class")

parent = Parent()
#print(parent.firstName)
print("---------------------")
#class Parent:
  #  firstName = "Jahanzeb"
    #lastName = "Naeem"

    #def __init__(self, fName, lName):
      #  self.firstName = fName
        #self.lastName = lName
        #print(self.firstName + " " + self.lastName)

   # def name(this):
     #   print(this.firstName + " " + this.lastName)

#parent = Parent("Jahanzeb", "Naeem")
print("---------------------")
class Child(Parent):
    def parentDetails(this):
        super().parentDetails()
        print("This is from child class")
    
    def childDetails(this):
        print("This is the last name : " + super().lastName)
child = Child()
child.childDetails()
child.parentDetails()








