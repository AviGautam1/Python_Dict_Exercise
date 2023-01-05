# Write a Python program to add a key to a dictionary.

# A key-value pair is taken by the update() function and immediately added to the dictionary that already exists.

emp_details = {
    "Name" : "Avinesh Gautam",
    "Designation" : "Python Develper",
    "Employee ID" : 23213
}

print("Current Employee Details : ", emp_details)

emp_details.update({"Organization" : "Skilline.AI"})

print("\nAfter Updating Employee Details : ", emp_details)


'''
output = 
Current Employee Details :  {'Name': 'Avinesh Gautam', 'Designation': 'Python Develper', 'Employee ID': 23213}

After Updating Employee Details :  {'Name': 'Avinesh Gautam', 'Designation': 'Python Develper', 'Employee ID': 23213, 'Organization': 'Skilline.AI'}
'''