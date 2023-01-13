import re


with open('assets/potential_contacts.txt') as file:
    potential_contacts = file.read()

# Regex to find telephone number

telephone_number = []
telephone_number.extend(
    re.findall('\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}',
               potential_contacts))

# To prevent duplicates
duplicate_phone = list(set(telephone_number))
duplicate_phone.sort()

phone_number = ''
for num in duplicate_phone:
    phone_number += num + ', '

# E-Mail Address

email_address = []
email_address.extend(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", potential_contacts))

email_remove_duplicates = list(set(email_address))
email_remove_duplicates.sort()

email_string = ''
for string in email_remove_duplicates:
    email_string += string + ', '

# to write to new documents

with open('assets/new_phone_numbers.txt', 'w') as file:
    phone_number_only = file.write(phone_number)

with open('assets/email_address.txt', 'w') as file:
    email_address_only = file.write(email_string)