from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns
data = fetch_california_housing(as_frame=True)
df = data.frame
fig, axes = plt.subplots(3, 3, figsize=(10, 8))
df.hist(bins=30, ax=axes.flatten(), color='skyblue', edgecolor='black', grid=False)
plt.suptitle('California Housing Dataset - Distribution of Features', fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
fig, axes = plt.subplots(3, 3, figsize=(10, 8))
axes = axes.flatten()
for i, col in enumerate(df.columns):
    sns.boxplot(x=df[col], ax=axes[i], color='lightgreen')
    axes[i].set_title(col, fontsize=10)
    axes[i].set_xlabel('')

plt.suptitle('California Housing Dataset - Box Plots', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()