# Annual-Income-Prediction

**Objective:**

To predict if the annual income of a given set of people is above or below $50K using various Machine Learning algorithms. 

**Methodology:**
 1. Preprocessing:
    * Read the dataset into a Pandas DataFrame using the read_csv function. The column headers were not supplied
      as a part of the dataset but were available externally, and hence were added to the dataset at the time of reading the         dataset.
    * The spaces before each of the string values in the dataset had to removed.
    * The dataset had ten columns in total. The first 9 columns - Age, Workclass, Education, Marital_Status, Occupation,  
      Race, Sex, Hours, and Country are the independent variables(X) and the last column is the target variable(y).
    * The categorical features - Workclass, Education, Marital_Status, Occupation, Race, Sex, and Country are convered into           Binary features. After binarizing the features, the matrix X has 94 dimensions.

2. Applying Classification algorithms:
    *  Since the output variable is discrete, this problem is a classification problem.
    * The first classification technique used was the Logistic Regression from the SciKit Learn package.
    * 20% of the dataset is set apart as the test set.
    * For now only Logistic Regression is used. **TODO:** Support Vector Machines, Random Forest, Decision Trees, etc.

3. Results:
    * Accuracy of the Logistic Regression model is around 82.96%. 
