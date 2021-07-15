import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

log = open('log.txt', 'r').readlines()[:-1]
best_values = [int(line.replace("\n", "").strip().split(": ")[2]) for line in log]

df = pd.DataFrame({'Nº Interation': range(len(log)), 'Best Value': best_values})
print(df.head())
sns_plot = sns.lineplot(data=df)
sns_plot.figure.savefig("output.png", x='Nº Interation', y='Best Value')