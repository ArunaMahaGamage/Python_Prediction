
import pandas as pd

from sklearn import tree
from sklearn.model_selection import train_test_split

class Model :

 def dayOfweek(self):
          df = pd.read_csv("acdents.csv")
          df.columns = ["X1", "X2", "X3", "X4","X5","X6","X7","X8","X9","X10","X11","X12","X13", "Y"]
          df.head()
          decision = tree.DecisionTreeClassifier(criterion="gini")
          X = df.values[:, 0:13]
          Y = df.values[:, 13]
          trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.5)
          decision = decision.fit(trainX, trainY)
          decision.predict([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])
          return (decision.score(testX, testY))
