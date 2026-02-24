import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("day9_tasks/train.csv")

# 条形图：不同性别生还率
rate = df.groupby("Sex")["Survived"].mean()
plt.bar(rate.index, rate.values)
plt.title("Survival Rate by Sex")
plt.ylabel("Rate")
plt.show()

# 饼图：生还 / 死亡比例
counts = df["Survived"].value_counts()
plt.pie(counts.values,labels=["Died", "Survived"],autopct="%.1f%%")
plt.title("Survival Distribution")
plt.show()