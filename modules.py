# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
# import datetime  # Import the entire module
# today = datetime.date.today()
# print(today)

# from datetime import date # Import only part of module that is needed
# today = date.today()
# print(today)

# import time 
# from time import time
# timestamp = time()
# print(timestamp)

# Pip modules
# from camelcase import CamelCase
# camel = CamelCase()
# text= 'hello there world'
# print(camel.hump(text))

# Custom modules
import validator
email = 'test@test.com'

if validator.validate_email(email):
  print('Email is valid')
else:
  print('Not an email')