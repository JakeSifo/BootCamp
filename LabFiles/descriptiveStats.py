import numpy as np 
import pandas as pd


################################################
# Computing Descriptive Statistics Using pandas
################################################

# Will calculate summary statistics of data

def usingNumpy():
    # Across the multi-dimensional array
    # pandas' DF offers these statistics column-wise
    normDist = 3 * np.random.randn(3,20) + 10 # mu = 10, sigma = 3
    print("Mean: ", normDist.mean())
# 10.079878379436774

    print ("Standard deviation: ", normDist.std())
#3.0549478985889276

def createDF ():
    import sys
    col1 = range(50)
    #col2 = [i for i in range(0,100,2)]
    col2 = np.random.exponential (0.5, 50)
    col3 = 4 * np.random.randn (50)  + 20
    col4 = 2 * np.random.randn (50)  + 40
  #  data = np.array([col1, col2, col3]).reshape(50,3)

    data = { 
        'range' : col1,      
        'expon' : col2,     
        'randn_m20_s4' : col3,
        'randn_m40_s2' : col4,
     }

    df = pd.DataFrame(data)
   # print (df.head())
    df.to_clipboard()

    print(df.shape)

    #print(df.to_json())

    df.to_csv("data_files/out.df.dat", sep="|", index=False)
    return df

def readDF():
    df = pd.read_table('data_files/out.df.dat' , sep='|')
    return df

createDF()
df = readDF()
print(df.head())

def printStatSummary(df, colName):
    print ("Summary statistics for ", colName)
    print("*" * 80)
    print("Mean value: \t\t", df[colName].mean())
    print("Standard Deviation: \t", df[colName].std())
    print("Skewnewss: \t\t", df[colName].skew())
    print("Kurtosis:  \t\t", df[colName].kurt())
    print("=" * 80)


printStatSummary(df, 'randn_m20_s4')
printStatSummary(df, 'randn_m40_s2')
printStatSummary(df, 'range')
printStatSummary(df, 'expon')

print ("Pairwise correlation of columns, excluding NA/null values: \n",df.corr())
print ("Pairwise covariance of columns, excluding NA/null values: \n",df.cov())

print ("Full descriptive statistical summary:\n", df.describe())
