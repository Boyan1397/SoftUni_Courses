def multiply_nums(num1, num2): #1.parameters\
    result = num1 * num2 #3.presmetni i dai resultata
    return result #2.vurni dadena stoinost(rezultata)

print(multiply_nums(5, 6))  #0 vij kakvo se iska#4 izvikai rezultata
print(multiply_nums(234, 325))
print(multiply_nums(-5,-6))

#kak se formira-| def - keyword
#EXAMPLE 1|
#def function_name(parameter: type):
    #statements(s)
#def some_func(number):
    #print(f"Count of {number}")
#for el in range(1,11):
    #some_func(f"numbers is {el}")
#EXAMPLE 2||
#def full_name(first_name, second_name):
    #print(f"First name is {first_name} and second is name {second_name}.")

#first = input("Enter first name")
#second = input("Enter second name")
#full_name(first,second)
#EXAMPLE 3|||
#def give_top():
    #print("This is top")
#def give_mid():
    #print("This is mid")
#def give_bot():
    #print("This is bot")
#def whole_column():
    #give_top()
    #give_mid()
    #give_bot()
#whole_column()
#####
#|||||direktno
#def give_me_number():
    #return 4
#print(give_me_number())
#||||| default arg
#def print_name(name= "Test"): #parameter by default
    #print(f"Hello, {name}!")

#print_name("Vanko") #argument that can be changed
def is_even(n):
    return n % 2 != 0


nums = [5,7,8,3,42,3,343,1,2,98]
evens = list(filter(is_even,nums))
print(evens)
