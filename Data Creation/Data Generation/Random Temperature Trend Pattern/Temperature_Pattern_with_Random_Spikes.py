## Load Library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.DataFrame()
signal_suuden_rise_fall=[]

#Random failure point
for i in range(100):
    
    #Noise creation numpy.random.normal(loc=0.0, scale=1.0, size=None)
    Noise=np.random.normal(0,1,90)
    #Consider avg temp is 30 and add noise
    signal= 30 + Noise
    random=np.random.randint(1,90, size=10)
    signal_sensor_fail=np.insert(signal,random,0)
    plt.plot(signal_sensor_fail)
    plt.title("Signal due to sensor failure")
    plt.show()
    tempdf=pd.DataFrame({'Pattern': ["signal_sensor_fail"]})
    tempdf=tempdf.join(pd.DataFrame([signal_sensor_fail]))
    df=df.append(tempdf, ignore_index=True)


for i in range(100):
    Noise=np.random.normal(0,1,100)
    signal_suuden_rise_fall[:]=30+Noise
    a=np.random.randint(1,50)
    b=np.random.randint(55,90)
    #print(a,b)
    signal_suuden_rise_fall[a:b]=np.random.randint(65,70, size=b-a)
    plt.plot(signal_suuden_rise_fall)
    plt.title("failure")
    plt.show()
    tempdf=pd.DataFrame({'Pattern': ["signal_suuden_rise_fall"]})
    tempdf=tempdf.join(pd.DataFrame([signal_suuden_rise_fall]))
    df=df.append(tempdf, ignore_index=True)
    

    
#print(df)
df.to_csv('Pattern.csv',index=False)