from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns
data = fetch_california_housing(as_frame=True)
df = data.frame
# Correlation Matrix Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, square=True)
plt.title('Correlation Matrix Heatmap', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()
sns.pairplot(df.sample(500), diag_kind='kde', plot_kws={'alpha': 0.6, 's': 30, 'edgecolor': 'k'})
plt.suptitle('California Housing Dataset - Pair Plot (Sampled)', fontsize=16, fontweight='bold', y=1.02)
plt.show()