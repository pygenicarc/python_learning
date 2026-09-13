his_name = "Subbu"
# print(his_name)
# subbu: {"name": "Subbu"}
# personal details

# lst = [1, 3, 4, 5, 'subbu', 'hello', 6, 7, 8, 9, 10]

his_details = {
    "name": his_name,
    "age": 25,
    "city": "Chennai",
    "email": "subbu@example.com",
    "phone": "123-456-7890",
    "address": "123 Main St, Chennai, India",
}

print(his_details.items())  # prints the values of the dictionary containing personal details

for i in his_details.items():
    print(f"{i}")  # prints each key-value pair in the dictionary


for key, value in his_details.items():
    print(f"{key}: {value}")  # prints each key-value pair in the dictionary

for key in his_details.keys():
    print(key)  # prints each key and its corresponding value in the dictionary

for value in his_details.values():
    print(value)  # prints each value in the dictionary