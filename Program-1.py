# Write a Python program to sort (ascending and descending) a dictionary by value.

dict_items = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original Dictinary Is : ", dict_items)

lst = list(dict_items.items())              # Convert it in a list.
lst.sort()
print("\nAscending Order Is : ", lst)

lst = list(dict_items.items())
lst.sort(reverse=True)                      # sort in reverse order
print("\nDescending Order Is : ", lst)

dict = dict(lst)                            # convert the list in dictionary
print("\nDictionary Is : ", dict)


'''
output = 
Original Dictinary Is :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

Ascending Order Is :  [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]

Descending Order Is :  [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]

Dictionary Is :  {4: 3, 3: 4, 2: 1, 1: 2, 0: 0}
'''

