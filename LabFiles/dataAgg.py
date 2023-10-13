import pandas as pd 
import numpy as np 


def setFactors(i):
    if i > 700:return 'LARGE'
    if i > 300:return 'MEDIUM'
    return 'SMALL'

def createDF ():
    len = 26
    col1 = [ch for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
   # col1 = (1000 * np.random.rand (len)).astype(int32) # -100, 100
    col2 = (1000 * np.random.rand (len)).astype(np.int32) # -100, 100
    col3 = [setFactors(i) for i in col2]
    col4 = ['DOWN', 'DOWN',  'UP', 'DOWN', 'DOWN',  'UP',  'UP', 'DOWN', 'DOWN',
        'UP',  'UP', 'DOWN', 'DOWN',  'UP', 'DOWN',  'UP',  'UP',  'UP',
        'UP',  'UP', 'DOWN', 'DOWN',  'UP', 'DOWN',  'UP', 'DOWN']

    data = { 'KPI' : col1, 'Value' : col2, 'Scale': col3, 'Movement' : col4 }
    return pd.DataFrame(data, columns=['KPI', 'Value', 'Scale', 'Movement'])

# df = createDF()
# print (df)

# df.to_csv("data_files/group_agg.dat", sep="|", index=False)

df = pd.read_table('c:/LabFiles/data_files/group_agg.dat' , sep='|')

groupValueByScale = df['Value'].groupby([df['Scale']])
# A more compact syntax: df.groupby(['Scale'])['Value'].mean()

print("\nThe Mean of Values Grouped by Scale: \n",  groupValueByScale.mean())
print("\nThe Max of Values Grouped by Scale: \n",   groupValueByScale.max())
print("\nThe Count of Values Grouped by Scale: \n", groupValueByScale.count())
print("\nThe Sum of Values Grouped by Scale: \n",   groupValueByScale.sum())



groupValueByScaleAndMovement = df['Value'].groupby([df['Scale'], df['Movement']])
# More compact syntax: groupValueByScaleAndMovement2 = df.groupby(['Scale', 'Movement'])['Value'].mean()

print("The Mean of Values Grouped by Scale & Movement: \n", groupValueByScaleAndMovement.mean())


# Pivot tables (spread rows into columns)

dfPivo = df.pivot(index = 'KPI', columns = 'Movement', values = 'Value')
print("\nThe Pivot table\n", dfPivo)
dfPivo.fillna('-', inplace =True)
print("\nThe Pivot table with NaN replaced\n", dfPivo)

df['Value'] = df['Value'].map(lambda x: '$' + str(1000 * x))
print("\nThe Data Frame  formatted with the map operation\n", df)


# Cross-tabulation
dfXT = pd.crosstab(df['Scale'], df['Movement'] )

print ("\nCrosstab: \n", dfXT)

# Compare (same, but a different layout, though): 
groupMovementsByScale = df['Movement'].groupby([df['Scale'], df['Movement']])

print("\nThe Count of Movements Grouped by Scale: \n", groupMovementsByScale.count())
print ("Done ...")
