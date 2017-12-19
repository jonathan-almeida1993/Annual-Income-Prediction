import pandas as pd

#Read training set into a DataFrame
dataset = pd.read_csv("income-data/income.train.txt",names=["Age","Workclass",\
                        "Education","Marital_Status","Occupation","Race","Sex","Hours","Country","Target"])

#removing spaces from the values
dataset["Target"] = dataset.loc[:,"Target"].str.strip()
dataset["Workclass"] = dataset.loc[:,"Workclass"].str.strip()
dataset["Education"] = dataset.loc[:,"Education"].str.strip()
dataset["Marital_Status"] = dataset.loc[:,"Marital_Status"].str.strip()
dataset["Occupation"] = dataset.loc[:,"Occupation"].str.strip()
dataset["Race"] = dataset.loc[:,"Race"].str.strip()
dataset["Sex"] = dataset.loc[:,"Sex"].str.strip()
dataset["Country"] = dataset.loc[:,"Country"].str.strip()

#Identify categorical features
categorical_features = [1,2,3,4,5,6,8]

#independent variables
X = dataset.iloc[:,:-1].values

#dependent variables
y = dataset.iloc[:,-1].values


#Binarize the categorical features
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
labelencoder_X = LabelEncoder()
for feature in categorical_features:
    X[:,feature] = labelencoder_X.fit_transform(X[:,feature])

onehotencoder = OneHotEncoder(categorical_features=categorical_features)
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)  

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=0)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

#Predict the results on the Test set
y_pred = classifier.predict(X_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

correct_predictions = len(y_test[y_test==y_pred]) #cm[0,0]+cm[1,1]
incorrect_predictions = len(y_test[y_test!=y_pred])#cm[0,1]+cm[1,0]
print("Number of correct predictions = {0}".format(correct_predictions))
print("Number of incorrect predictions = {0}".format(incorrect_predictions))
print("ACCURACY = {0}".format(correct_predictions/len(y_test)))

