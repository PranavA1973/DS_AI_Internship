import pandas as pd

grades=pd.Series([85, None, 92, 45, None, 78, 55])

missingvalue=grades.isnull()
print(missingvalue)

fillingvalues=grades.fillna(0)
print(fillingvalues)

filtered_grades =grades[grades > 60]
print(filtered_grades)