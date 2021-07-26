import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./result/test_url1_raw_data_75737.csv", header = None, index_col=0).T
# # df.boxplot(grid=False, rot=45, fontsize=13)

fig, axs = plt.subplots(1,2)
res1 = df.filter(regex=("read.*1"))
sns.boxplot(data=res1, palette="Set3", ax= axs[0])


res2 = df.filter(regex=("read.*2"))
sns.boxplot(data=res2, palette="Set3", ax=axs[1])

# plt.xticks(rotation=-50)
for ax in axs:
    plt.sca(ax)
    plt.xticks(rotation=-50)
plt.tight_layout()
plt.show()