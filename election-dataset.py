import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections
df=pd.DataFrame()
for f in["C:\\Datasheets\\2009maharashtraresults.xlsx","C:\\Datasheets\\2014maharashtraresults.xlsx"]:
    data=pd.read_excel(f,'Sheet1')
    df=df.append(data)
df.to_excel("C:\\Datasheets\\combine.xlsx")
data=pd.read_excel("C:\\Datasheets\\combine.xlsx")
print(data)
plt.figure(figsize=(8,4))
plt.scatter(data['PARTYNAME'],data['SEATS'],c='blue')
plt.xlabel("Party")
plt.ylabel("Seats won")
plt.xticks(rotation=90)
plt.show()
final_Data={}

for i in data['PARTYNAME']:
    x=i
    t1=(data[(data.PARTYNAME==x)&(data.YEAR==2009)].SEATS).tolist()#retriving the data and saving it in panda.seriesdatatype
    t2=(data[(data.PARTYNAME==x)&(data.YEAR==2014)].SEATS).tolist()#same
    t3=t2+t1#concanicates the list
    print("------------------")
    print("Name of party=",i)
    print("Number of seats=",int(sum(t3)))
    final_Data.update({i:int(sum(t3))})
plt.bar(final_Data.keys(),final_Data.values(),color='green')
plt.xlabel("Party")
plt.ylabel("Seats Won")
plt.xticks(rotation=90)
#print("The change")
#for i in data['PARTYNAME']:
#    x=i
'''    t1=(data[(data.PARTYNAME==x)&(data.YEAR==2009)].SEATS).tolist()#retriving the data and saving it in panda.seriesdatatype
    t2=(data[(data.PARTYNAME==x)&(data.YEAR==2014)].SEATS).tolist()
    diff=sum(t1[0:])-sum(t2[0:])
    if diff>0:
        print("Party Name",x)
        print("Loss in seats=",int(diff))
    elif diff<0:
        print("Party Name",x)
        print("Gain in seats=",abs(int(diff)))
    else:
        print("Party Name",x)
        print("No change in seats")
        '''
        