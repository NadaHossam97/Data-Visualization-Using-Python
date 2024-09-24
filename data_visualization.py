import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib import pyplot
import seaborn as sns
from ucimlrepo import fetch_ucirepo 


adult = pd.read_csv(".\\adult.csv", header=0)
#handling missing values:
# replace "?" to NaN
adult.replace("?", np.nan, inplace = True)

# Check if there are any missing values in the entire dataset
missing_before_replacement = adult.isnull().sum()

# Print the missing values for each column
print("Missing values after replacement in each column:")
print(missing_before_replacement)

# Replace missing values in 'workclass' with the most frequent value
most_frequent = adult['workclass'].mode()[0]  # Get the mode
adult['workclass']=adult['workclass'].fillna(most_frequent)  # Replace missing values

# Replace missing values in 'Occupation' with the most frequent value
most_frequent = adult['occupation'].mode()[0]  # Get the mode
adult['occupation']=adult['occupation'].fillna(most_frequent)  # Replace missing values

# Replace missing values in 'native-country' with the most frequent value
most_frequent = adult['native-country'].mode()[0]  # Get the mode
adult['native-country']=adult['native-country'].fillna(most_frequent)  # Replace missing values

# Check if there are any missing values in the entire dataset
missing_after_replacement = adult.isnull().sum()

# Print the missing values for each column
print("Missing values after replacement in each column:")
print(missing_after_replacement)

#data normalization
adult['age']=adult['age']/adult['age'].max()
adult['fnlwgt']=adult['fnlwgt']/adult['fnlwgt'].max()
adult['education-num']=adult['education-num']/adult['education-num'].max()
adult['capital-gain']=adult['capital-gain']/adult['capital-gain'].max()
adult['capital-loss']=adult['capital-loss']/adult['capital-loss'].max()
adult['hours-per-week']=adult['hours-per-week']/adult['hours-per-week'].max()

#creating dummy variable for workclass
dummies=pd.get_dummies(adult,columns=['workclass','education','marital-status','occupation','relationship','race','sex'])
print(dummies)



#data visualization
# Bar plot for categorical variables
sns.countplot(data=adult, x='workclass')
plt.title('Distribution of Workclass')
plt.xticks(rotation=45)
plt.show()

sns.countplot(data=adult, x='education')
plt.title('Distribution of Education')
plt.xticks(rotation=90)
plt.show()


# Histogram for numeric columns
plt.figure(figsize=(8, 6))
sns.histplot(adult['age'], kde=True, bins=30)
plt.title('Distribution of Age')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(adult['hours-per-week'], kde=True, bins=30)
plt.title('Distribution of Hours Per Week')
plt.show()

# Boxplot for numerical variables
plt.figure(figsize=(8, 6))
sns.boxplot(x=adult['age'])
plt.title('Boxplot of Age')
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x=adult['hours-per-week'])
plt.title('Boxplot of Hours Per Week')
plt.show()

# Correlation matrix for numerical variables
plt.figure(figsize=(10, 8))
sns.heatmap(adult.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

# Workclass vs Income
sns.countplot(data=adult, x='workclass', hue='income')
plt.title('Workclass vs Income')
plt.xticks(rotation=45)
plt.show()

sns.pairplot(adult, hue='income', vars=['age', 'hours-per-week', 'education-num'])
plt.show()

print(adult)