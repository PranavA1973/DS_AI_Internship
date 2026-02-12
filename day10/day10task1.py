import pandas as pd
#df=pd.DataFrame({
    #"Name":['Prnv',"satwk","bhansh"]
    #})
#print(df)

#data =({"prnv"})
#print(pd.DataFrame(data))#one more way to creat a dataframe

#df.index=[100,200,300]
#print(df)

df = pd.read_csv("orders.csv")
print("original dataset",df)

print("missing values\n",df.isna().sum())
print(df)

print("Handling missing values:\n")
df = df.fillna(df.median(numeric_only=True))
print(df)

duplicates = df.duplicated()

print("Duplicate Rows:\n")
print(duplicates)

print("Actual Duplicate Rows:\n")
print(df[df.duplicated()])

df = df.drop_duplicates()
print(df)
