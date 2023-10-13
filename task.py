import random
import pandas as pd

# pd.get_dummies(data['whoAmI'])

lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)

df = pd.DataFrame({'whoAmI': lst})

df.loc[df['whoAmI'] == 'human', 'human'] = 'human'
df.loc[df['whoAmI'] == 'robot', 'robot'] = 'robot'

df = df.fillna(0)

df = df.replace(['human', 'robot'], [1, 1])

print(df[['human', 'robot']])
