import pandas as pd
# a=pd.read_csv("test3.csv")
a= pd.read_csv("test3.csv",names=['Name','Age','Div'],skiprows=[2,3])
# a = a.drop()
print(a)