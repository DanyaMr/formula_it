import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

iris = sns.load_dataset("iris")

x = iris[iris['species'] != 'virginica'].iloc[:, 0:2].to_numpy()

model = KMeans(n_clusters=2, random_state=42, n_init=10)

model.fit(x)

xx, yy = np.meshgrid(
    np.linspace(x[:, 0].min() - 0.5, x[:, 0].max() + 0.5, 100),
    np.linspace(x[:, 1].min() - 0.5, x[:, 1].max() + 0.5, 100),
)

Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

x_0 = iris[iris['species'] == 'setosa'].iloc[:, 0].to_numpy()
y_0 = iris[iris['species'] == 'setosa'].iloc[:, 1].to_numpy()
x_1 = iris[iris['species'] == 'versicolor'].iloc[:, 0].to_numpy()
y_1 = iris[iris['species'] == 'versicolor'].iloc[:, 1].to_numpy()

ax = plt.gca()
ax.contourf(xx, yy, Z, alpha=0.3, levels=[-0.5, 0.5, 1.5], cmap='coolwarm')

plt.scatter(x_0, y_0, color="red", alpha=0.5, label="реальная setosa")
plt.scatter(x_1, y_1, color="green", alpha=0.5, label="реальная versicolor")

plt.title("K-Means: Обучение без учителя (кластеризация)")
plt.legend()
plt.show()
