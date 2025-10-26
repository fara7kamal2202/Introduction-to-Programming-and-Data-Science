from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier



X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

clf = KNeighborsClassifier()
clf.fit(X_train_scaled, y_train)
score = clf.score(X_test_scaled, y_test)

single_instance = X_test_scaled[0]
print(clf.predict([single_instance]))
print(clf.predict_proba([single_instance]))
