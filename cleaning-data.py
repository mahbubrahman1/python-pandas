
# import pandas as pd

# df = pd.read_csv('data.csv')

# df.dropna(inplace = True)

# print(df.to_string())



# Remove all rows with NULL values
# import pandas as pd 

# df = pd.read_csv('data.csv')

# df.dropna(inplace = True)

# print(df.to_string())



# Convert to date
# import pandas

# df = pandas.read_csv('data.csv')

# df['Date'] = pandas.to_datetime(df['Date'])

# print(df.to_string())


# Replacing Values
# import pandas as pd

# df = pd.read_csv('data.csv')
# df.loc[7, 'Duration'] =  45

# print(df.to_string())



# Removing Duplicates
import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())