## Load Library
import pandas as pd
import numpy as np

## Load the data which already as one_to_one Mapping. It was done in each of the Data Generation codes
data=pd.read_csv('rise_train_data_single_cause.csv')

## Convering pandas into numpy
linear_rise=np.array(data[0:100])

## Shuffle the dataset
np.random.shuffle(linear_rise)

## Get the shape
size=linear_rise.shape[0]
index=linear_rise.shape[1] -1

## Assigning 70% to Oil Leakage
ratio=int(size * 0.7)
linear_rise[0:ratio,index]='Oil Leakage'

## Remaining 20% to Cooling System Issues
ratio1=int(size *0.2)+ratio
linear_rise[ratio:ratio1,index]='Cooling system issues'

## Remaining to Generator Speed descrepancy
linear_rise[ratio1:,index]='Generator speed discrepancies'

## Shuffle It again
np.random.shuffle(linear_rise)

## Convert to csv
linear_rise=pd.DataFrame(linear_rise)
linear_rise.to_csv('linear_rise.csv',index=False)
