import random

# Define the possible values for each key
countries = ['USA', 'Canada', 'UK', 'Germany']
ages = [20, 25, 30, 35]
years = [2000, 2001, 2002, 2003]

# Create a dictionary with random values for each key
data_dict = {'country': [], 'age': [], 'year': []}
for i in range(4):
    data_dict['country'].append(random.choice(countries))
    data_dict['age'].append(random.choice(ages))
    data_dict['year'].append(random.choice(years))

# Print the dictionary
print(data_dict)

