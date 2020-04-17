# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
print(fruit_tuple)

# Using contructor
fruit_tuple_2 = tuple(('Apple', 'Orange', 'Mango'))

# Get single value
print(fruit_tuple[1])

# Cannot change value
# fruit_tuple[1] = 'Grape' # error

# Tuple with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

# Get len
print(len(fruit_tuple))

# Delete tuple
del fruit_tuple # del keyword for delete

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}
print(fruit_set)

# Check if in set
print('Apple' in fruit_set) # True
print('Apples' in fruit_set) # False

# Add to set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Grape')

# Clear set
fruit_set.clear()

# Delete set
del fruit_set 

