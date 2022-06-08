# import pandas

# info = {
# 	"Student Name": ["Nadim", "Joni", "Rayan"],
# 	"CGPA": [3.89, 4.00, 3.44]
# }

# # load data into a DataFrame object
# result = pandas.DataFrame(info)

# print(result)


"""
import pandas

person = {
	"Name": ["John", "Smith", "Emei", "David"],
	"ID": [1065, 1089, 1034, 1021],
	"Address": ["Toronto, Canada", "Hong Kong, China", "Silicon Valley, US", "Tokyo, Japan"]
}

result = pandas.DataFrame(person)

print(result)
"""

#------------------------------

# Locate Row
# Pandas use the loc attribute to return one or more specified row(s)

# import pandas

# person = {
# 	"Name": ["John", "Smith", "Emei", "David"],
# 	"ID": [1065, 1089, 1034, 1021],
# 	"Address": ["Toronto, Canada", "Hong Kong, China", "Silicon Valley, US", "Tokyo, Japan"]
# }

# result = pandas.DataFrame(person)

# print(result.loc[2])


#------------------------------

# Named Indexes
# With the index argument, you can name your own indexes.

import pandas

person = {
	"Name": ["John", "Smith", "Emei", "David"],
	"ID": [1065, 1089, 1034, 1021],
	"Address": ["Toronto, Canada", "Hong Kong, China", "Silicon Valley, US", "Tokyo, Japan"]
}

result = pandas.DataFrame(person, index = ["Canadian", "American", "Chinese", "Japanese"])

print(result)