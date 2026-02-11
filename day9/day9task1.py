import pandas as pd

products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard'])

laptopprice = products['Laptop']

firsttwo = products.iloc[0:2]
#products.loc['Laptop':'Mouse'] Accessing using labels

print("Full Series:\n")
print(products)

print("\nAccessing the price of laptop:",laptopprice)

print("\nfirst two products are:\n",firsttwo)
