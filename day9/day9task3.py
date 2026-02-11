import pandas as pd

usernames=pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

print("space removed\n",usernames.str.strip())

print("lower case\n",usernames.str.lower())

print("Letters that contains a\n",usernames.str.contains('a'))