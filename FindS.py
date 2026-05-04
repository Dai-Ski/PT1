import pandas as pd
data = pd.read_csv('data.csv')
concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values
h = concepts[0].copy()
for i, val in enumerate(concepts):
    if target[i] == "Yes":
        for x in range(len(h)):
            if h[x] != val[x]:
                h[x] = '?'
print(h) 
