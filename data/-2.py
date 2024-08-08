import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

header = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=header)
# data.describe().to_csv('./result/pima_describe.csv')
# corr = data.corr(method='pearson')

plt.clf()
# data.hist(figsize=(12,10),bins=5)
# plt.tight_layout()
# plt.savefig("./result/hist.png")
pd.plotting.scatter_matrix(data)


# data.plot(kind="density",subplots=True, figsize=(12,10),layout=(3,3), sharex=False,sharey=False)
plt.savefig("./result/scatter.png")