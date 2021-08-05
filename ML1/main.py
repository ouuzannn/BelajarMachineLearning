from sklearn.datasets import load_iris

iris = load_iris()
# print(iris)

# print(iris.keys())

#deskripsi sample dataset

# print(iris.DESCR)

# akses explanatory = features, response = target

# explanatory 
x = iris.data
print(x)

# response
y = iris.target
print(f'{y}\n')

#featur & target names

#feature name (representasi kolom)
feature_names = iris.feature_names
print(f'{feature_names}\n')


#target Name
target_name = iris.target_names
print(f'{target_name}\n')
