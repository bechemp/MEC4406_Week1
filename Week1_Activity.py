# write code in python that prints your name

MyName = "Rebecca"

print(MyName)

# and then counts up your favourite number squared

favourite_number = 3

print(favourite_number * favourite_number)

# commit this code to your own GitHub

# update the code to contain a class Engineers with a fixed class attribute skill equal to "problem solver" and initial attributes name, type, years of experience.

skill = ("problem solver")

class Engineers:
  def __init__ (self, skill, name, type, years_of_experience):
    self.skill = ("problem solver")
    self.name = name
    self.type = type
    self.years_of_experience = years_of_experience
  
# create two different engineers (objects) and print out their variables

engineer1 = Engineers(skill, "Susan", "mechanical", 25)
engineer2 = Engineers(skill, "Peter", "environmental", 2)

print (vars(engineer1))
print (vars(engineer2))

# also change your name to be the reverse

NewName = MyName [::-1]
print(NewName)

# commit this new code t your GitHub