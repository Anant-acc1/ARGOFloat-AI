import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_parquet('parquet_files/nodc_1900121_prof.parquet')
df.plot()
plt.show()
print(df)
