# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}
print(person)

# Using a contructor
person_2 = dict({
  'first_name':'John',
  'last_name':'Doe',
  'age':30
})
print(person_2)

# Access a single value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get keys 
print(person.keys())

# Get items
print(person_2.items())

person_3 = person.copy()

person_3['city'] = 'Boston'
print(person_3)


# Remove item
del(person['age'])
print(person)

person.pop('phone')

# Clear
person.clear()

# Get Len
print(len(person_2))


# List of Dictionary
people = [
  {'name': 'Martha', 'age': 40},
  {'name': 'Bob', 'age': 20}
]
print(people[1]['name'])





