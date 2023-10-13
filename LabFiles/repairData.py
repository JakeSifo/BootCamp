from sklearn import preprocessing
import pandas as pd
import numpy as np

nan = np.nan  # Not a Number (NULL, N/A)

r1 = [11,12,nan]
r2 = [nan,22,nan]
r3 = [31,nan,33]
r4 = [41,42,43]

dataSet = pd.DataFrame([r1, r2, r3, r4])

print (dataSet)
print("Original DF shape: ", dataSet.shape)
# axis = 0 - columnwise
print (dataSet.isnull().sum(axis = 0))  

# axis = 1 - rowwise
#print (dataSet.isnull().sum(axis = 1))


# Dropping the 3rd column
dataSet2 = dataSet.drop(2, axis=1)

print (dataSet2)
print("Updated DF shape: ", dataSet2.shape)

# Adding a column of zeros 
nRows =len(dataSet2.index) # Not .count() function excludes NaN
# You can also find the shape of the Data Frame and select the first index (rows)
# df.shape --> (nrows, ncols)  like so: df.shape[0] - number of rows, df.shape[1] - num of columns


# Here is how you can add a colum with zeros for values:
#dataSet2[2] =  np.zeros(nRows, dtype=int)  # [0,0,0,0]  # or 

#print (dataSet2)
#print("Updated DF shape: ", dataSet2.shape)

# Interpolating the values in column 1
dataSet2[0].interpolate(method = "nearest", inplace=True)  # Updating the self instance
#Try this one.  Note: Comment out the previous code line with the nearest method.
#dataSet2[0].interpolate(method = "linear", inplace=True)  # Updating the self instance

#Note: All the supported methods for interpolation:
#method : {‘linear’, ‘time’, ‘index’, ‘values’, ‘nearest’, ‘zero’,
# ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘krogh’, ‘polynomial’,
#  ‘spline’, ‘piecewise_polynomial’, ‘from_derivatives’, ‘pchip’, ‘akima’}



# Replacing missing values in the second column with the mean value
dataSet2[1].fillna(dataSet2[1].mean(), inplace=True)   # Updating the self instance
print (dataSet2)


# Scaling data
# In practice we often ignore the shape of the distribution and just transform the data to center 
# it by removing the mean value of each feature, 
# then scale it by dividing non-constant features by their standard deviation.


toScaleDS = np.ceil(100 * np.random.rand (10,4))
print(toScaleDS)

#
# X_train = np.array([[ 1., -1.,  2.],
#                     [ 2.,  0.,  0.],
#                    [ 0.,  1., -1.]])

#X_scaled = preprocessing.scale(X_train)

# Performs z-score normalizatoin 
# Center the mean to zero and decide the result by the standard deviation
# Most values should be in [-3, +3]
scaledDS = preprocessing.scale(toScaleDS)
print(scaledDS)
#inputData = preprocessing (toScale)
print(scaledDS.mean(axis = 0))  # array of column-wise (for each feature)  --> 0
print(scaledDS.std(axis = 0))   # array of sd values --> 1

print ( pd.DataFrame (scaledDS)[0].mean())

print( pd.DataFrame (scaledDS)[0].std())


# Scaling using min-max transformation
# Rescales the data set to values in the range of [0,1]

def minmaxTrans (dfIn):
    df = dfIn
    ncols = df.shape[1]
    for i in range(ncols):
      #  print ("Working on  column ", i)
        mi = min(df[i])
        ma = max(df[i])
        spread = ma - mi

        # print ("Min, max, spread ", mi, ma, spread)

        if spread == 0:
            return dfIn

        df[i] = (df[i] - mi) / spread

    # print ("Updated df, ", df)        
    return df

mmDF = minmaxTrans(pd.DataFrame(toScaleDS))
print("Custom min-max transformation:\n", mmDF)
print ("Custom min-max transformation min and max:\n",mmDF[0].min(axis=0), mmDF[0].max(axis = 0))


# scikit-learn preprocessing operates on arrays 
mmScaler = preprocessing.MinMaxScaler()
print("MinMaxScaler:\n", mmScaler.fit_transform(toScaleDS))