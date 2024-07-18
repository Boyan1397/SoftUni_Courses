class Phone:

    def __init__(self, color, size): #dunder-magic  !method!
        #color and type are the parameters
        self.color = color #instance variable  (ATRIBUTES)                    #state!!!!
        self.size = size  #instance variable   (ATRIBUTES) 

    def turn_on(self):  #public method                             #behaviour!!!!
        return "The phone is turned on"

p1 = Phone("purple", 15)  # Creating instances (objects) of the class Phone
# "purple" and 15 are arguments passed to the constructor


p2 = Phone("yellow", 120) # Creating instances (objects) of the class Phone
# "yellow" and 120 are arguments passed to the constructor

print(p2.turn_on())