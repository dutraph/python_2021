import datetime
name = "Paulo"
age = 30
height = 1.79
is_adult = age > 18
weight = 109
bmi = weight / (height ** 2)

this_year = datetime.date.today().year


# print(f'{name} is {age} years old, and his BMI is {bmi:.2f}.')
# print('{} is {} y.o and his BMI is {:.2f}'.format(name,age,bmi))

# print('{n} is {ag} y.o and his BMI is {bm:.2f}'.format(n=name,ag=age,bm=bmi))
# print('{0} is {1} y.o and his BMI is {2:.2f}'.format(name,age,bmi))


"""
Chalange 
"""

print(f'{name} is {age} years old, {height} tall and {weight}kg')
print(f"{name}'s BMI is {bmi:.2f}.")
print(f'{name} was born in {this_year - age}.')
