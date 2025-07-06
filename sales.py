import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# we are using pandas in this part 
df=pd.read_csv("data_analytics_projects/sales_data_dirty.csv")
print(df.head(5))

print(df.shape)

#print(df.isnull())
print(df.isnull().sum())

print(df.duplicated().sum())

print(df.columns)

#print(df["Region"].unique())
#print(df["Product"].unique())

df["Region"]=df["Region"].str.strip()
df["Region"]=df["Region"].str.title()
print(df["Region"].unique())

df["Product"]=df["Product"].str.title()
print(df["Product"].unique())

pd.to_datetime
print(df["Date"].head(5))

df["Finaltotal"]=df["Total"]-(df['Total']*df["Discount"])
print(df["Finaltotal"].head(5))

df["Revenueperunit"]=df["Total"]/df["Quantity"]
print(df["Revenueperunit"].head(5))
print(df["Revenueperunit"].isnull().sum())

print(df.groupby("Region")["Finaltotal"].max())

print(df.groupby("Product")["Total"].sum())

print(df.groupby("Category")["Discount"].mean())

filter_rows=df[(df["Quantity"]>10) & (df["Discount"]>0.05)]
print(filter_rows.head(5))

# we are using numpy in this part

arr=np.array(df["Discount"].values)
nul=np.isnan(arr)
arr[nul]=0
df["Discount"]=arr
print(df["Discount"].isnull().sum())


#print(df["Total"].isnull().sum())

mean=np.array(df["Total"].values)
tru=np.isnan(mean)
mean[tru]=df["Total"].mean()
df["Total"]=mean
print(df["Total"].isnull().sum())


arr=np.array(df["UnitPrice"].values)
print(arr.mean())
print(arr.std())


Condition1= df["UnitPrice"] < 20

Condition2= (df["UnitPrice"] >= 20) & (df["UnitPrice"] <= 40)

Condition3= df["UnitPrice"] > 40

choices=["low","mid","high"]

df["Pricebucket"]=np.select([Condition1,Condition2,Condition3],choices,default="unknown")
print(df["Pricebucket"].value_counts())


count=np.unique(df["Pricebucket"].values, return_counts=True)
print(count)

print(np.corrcoef(df["Quantity"],df["Total"]))


# we are using matplotlib

plt.subplot(2,2,1)
sales=df.groupby("Region")["Total"].sum()
plt.bar(sales.index,sales.values,color="blue",label="sales by region")
plt.xlabel("regions-->")
plt.ylabel("total sales-->")


plt.subplot(2,2,2)
pies=df.groupby("Category")["Total"].sum()
plt.pie(pies,labels=pies.index,autopct="%1.1f%%")


plt.subplot(2,2,3)
line=df.groupby("Date")["Total"].sum()
plt.plot(line.index,line.values)
plt.xticks(rotation=40)
plt.xlabel("dates-->")
plt.ylabel("total sales-->")

plt.suptitle("sales dataset vizualization")
plt.tight_layout()
plt.show()