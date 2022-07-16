import pandas as pd

df=pd.DataFrame({"a":[1,2,3,4],"b":[4.5,3,4,6]})
df.to_csv("report1.csv",index=False)


