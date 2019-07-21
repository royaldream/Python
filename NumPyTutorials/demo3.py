import numpy as np
import pandas as pd

print "sine"
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
data_set = {"x": x, "y": y}
df = pd.DataFrame(data_set)

print df

print df.head(2)
print df.tail(2)

print "merge"
df1 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"HPI": [80, 90, 70, 60], "Int_Rate": [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 67]},
                   index=[2005, 2006, 2007, 2008])

merged = pd.merge(df1, df2)

print(merged)
merged = pd.merge(df1, df2, on="HPI")

print(merged)
