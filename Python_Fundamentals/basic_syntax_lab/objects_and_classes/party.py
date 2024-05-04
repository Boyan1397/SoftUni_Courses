class Party:     #class - blueprint
    def __init__(self):
        self.people = []       #instance atributes


some_people = Party()          #object

names = input()
while names != "End":
    some_people.people.append(names)      #putting the atribute to the object

    names = input()
print(f"Going: {', '.join(some_people.people)}")
print(f"Total: {len(some_people.people)}""")

