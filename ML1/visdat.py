from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target


x = x[:, :2]

x_min, x_max = x[:, 0].min() - 0.5, x[:, 0].max() * 0.5
y_min, y_max = x[:, 1].min() - 0.5, x[:, 1].max() * 0.5


plt.scatter(x[:, 0], x[:, 1], c=y)
plt.xlabel('Sepal length')
plt.ylabel('sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.grid(True)
plt.show
