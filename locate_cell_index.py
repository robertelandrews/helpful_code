### Locate a row, column index when you don't know the index value but 
### know part of the string
df.loc[df['COLUMN'].str.contains('STRING', case=False)].index