# Pandas are predefined data structures that provide nice features for data handling
import pandas as pd

# Models from sklearn - KNN
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Read data, by specifying the file, delimiter and the header row
data = pd.read_csv('export.csv', sep=',', header=0)

# Print a short summary of the dataset
print(data.describe())

# Separate the independent (predictor) variables and the dependent variables (predicted)
x_data = data.filter(['comment_count','follows','followed_by','python_faces'], axis=1).fillna(0)
y_data = data.filter(['like_count'], axis=1).fillna(0)

# Split the dataset into train and test with a 80-20 ratio
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2)


best = -10000
best_n = 0
best_k = 0
for i in range(50):
    print("number of estimators = %s" % (i + 1))
    for k in range(25):
        forest = RandomForestRegressor(n_estimators=i+1, max_depth=k+1, n_jobs=-1)
        forest.fit(x_train, y_train.values.ravel())
        sc = forest.score(x_test, y_test)
        # print(sc)
        if sc > best:
            best = sc
            best_n = 1 + i
            best_k = 1 + k
            print("Better model with est=%s, depth=%s, score=%s" % (i + 1, k+1, best))



forest = RandomForestRegressor(n_estimators=best_n, max_depth=20, n_jobs=-1)
forest.fit(x_train, y_train.values.ravel())


# Generate the predicted column of data
y_predict = forest.predict(x_test)

# Store it in a panda dataframe for easier comparison with the true values
y_predict = pd.DataFrame(y_predict, y_test.index, columns=['predicted_like_count'])

# Concatenate the two columns for comparison
y_analysis = pd.concat([y_predict, y_test], axis=1)

# Display the two columns
print(y_analysis)

