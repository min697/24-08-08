import matplotlib.pyplot as plt
import pandas as pd
header = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv',
                   names=header)
# data.describe().to_csv('./result/pima_describe.csv')
corr = data.corr(method='pearson')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr, cmap='coolwarm', vmin=-1,vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xtickslabels(column_names)
ax.set_ytickslabels(column_names)
plt.show()
plt.savefig("./result/corr.png")