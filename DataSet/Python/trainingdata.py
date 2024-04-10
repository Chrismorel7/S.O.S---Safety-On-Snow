import pandas as pd

VIDEO = str(12548)
PATH = 'combineddata.csv'

df = pd.read_csv(PATH)
print(df.describe())

df1 = df[df['fall'] == 1.0]
print(df1.describe())

df0 = df[df["fall"] == 0.0]
df0 = df0.sample(n=1000, random_state=42)
print(df0.describe())


dfoutput = pd.concat([df0, df1])

#dfoutput = dfoutput.sample(frac=1, random_state=42)

dfoutput = dfoutput.drop(axis=1, columns={'oldindex'})

dfoutput.reset_index(drop=True, inplace=True)

print(dfoutput.describe())
dfoutput.to_csv("trainingdata.csv")