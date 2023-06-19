from collections import OrderedDict

# Create an empty ordered dictionary
ordered_dict = OrderedDict()

# Insert elements into the ordered dictionary
ordered_dict['apple'] = 3
ordered_dict['banana'] = 2
ordered_dict['orange'] = 5
ordered_dict['grape'] = 4

# Print the ordered dictionary
for key, value in ordered_dict.items():
    print(key, value)
