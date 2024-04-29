import pandas as pd

data = [['John', 45, 'Manager'], ['lisa', 34, 'Developer'], ['Thomas', 36, 'Tester'], ['Kaisy', 23, 'Tester'], ['Peter', 45, 'Manager'],
        ['Kindle', 45, None]]

df = pd.DataFrame(data, columns=['Name', 'age', 'Role'])

df.dropna(axis=0, inplace=True)

print(df)


