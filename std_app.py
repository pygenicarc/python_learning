his_name = "Subbu"
his_bank = ('hdfc', '1234567890', 'savings')
his_details = {
    "name": his_name,
    "age": 25,
    "city": "Chennai",
    "email": "subbu@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St, Chennai, India",
}

student1 = {
    "name": his_name,
    "age": 25,
    "city": "Chennai",
    "email": "subbu@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St, Chennai, India",
    "bank": his_bank[0],
    "account_number": his_bank[1],
    "account_type": his_bank[2],
}

student2 = {
    "name": his_name,
    "age": 25,
    "city": "Chennai",
    "email": "subbu@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St, Chennai, India",
    "bank": his_bank[0],
    "account_number": his_bank[1],
    "account_type": his_bank[2],
}
student3 = {
    "name": his_name,
    "age": 25,
    "city": "Chennai",
    "email": "subbu@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St, Chennai, India",
    "bank": his_bank[0],
    "account_number": his_bank[1],
    "account_type": his_bank[2],
}

personas = [student1, student2, student3]
print(personas)  # prints the list of dictionaries containing personal details of students

for persona in personas:
    print(persona)  # prints each dictionary in the list of dictionaries containing personal details of students