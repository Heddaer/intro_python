import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

sns.set_theme()

#tips = sns.load_dataset("DS_TUG_Floor1")



sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker", sytle="smoker", size="size",)

# ChatGPT
# data = np.random.rand(10,10)

# plt.imshow(data, cmap='hot', interpolation='nearest')
# plt.colorbar()
# plt.show()