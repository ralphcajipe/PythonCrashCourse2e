people = []

person = {'first_name': 'ralph',
          'last_name': 'cajipe',
          'age': 21,
          'city': 'santa rosa',
          }
people.append(person)

person = {'first_name': 'tony',
          'last_name': 'stark',
          'age': 35,
          'city': 'new york',
          }
people.append(person)

person = {'first_name': 'jarvis',
          'last_name': 'system',
          'age': 1,
          'city': 'artificial city',
          }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name}, of {city}, is {age} years old.")