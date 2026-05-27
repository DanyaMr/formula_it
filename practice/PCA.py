import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

iris = sns.load_dataset("iris")

x = iris[iris['species'] != 'virginica'].iloc[:, 0:4].to_numpy()

pca = PCA(n_components=2)

x_pca = pca.fit_transform(x)

x_0 = x_pca[0:50, 0]
y_0 = x_pca[0:50, 1] 
x_1 = x_pca[50:100, 0]
y_1 = x_pca[50:100, 1]

plt.scatter(x_0, y_0, color="red", alpha=0.5, label="setosa")
plt.scatter(x_1, y_1, color="green", alpha=0.5, label="versicolor")

plt.title("PCA")
plt.xlabel("Главная компонента 1")
plt.ylabel("Главная компонента 2")
plt.legend()
plt.show()
