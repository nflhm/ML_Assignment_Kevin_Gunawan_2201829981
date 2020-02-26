#!/usr/bin/env python
# coding: utf-8

# In[22]:
## Nama: Kevin Gunawan
## NIM: 2201829981

## 1. Data dari listings.csv dapat dipakai menggunakan supervised learning sebagai information retrieval atau 
##    menggunakan unsupervised learning untuk clustering data.


# In[20]:


## Import Data
import pandas as pd
listingsData = pd.read_csv("listings.csv", delimiter = ",")
print("Total data:", len(listingsData))
print("Any null values?:", listingsData.isna().values.any())
## print(listingsData)


# In[11]:


## Menampilkan Maximum & Minimum Value
print("Maximum:")
print(listingsData.max())
print("---------")
print("Minimum:")
print(listingsData.min())


# In[14]:


## Mengganti null value dengan " "
modifiedListings = listingsData.fillna(" ")
print("Any null values?:", modifiedListings.isna().values.any())
print("Total data:", len(modifiedListings))
## listingsData = listingsData.fillna(" ")


# In[17]:


## Me-remove semua baris yang memiliki null Values
removeListings = listingsData.dropna()
print("Any null values?:", removeListings.isna().values.any())
print("Total data:", len(removeListings))
## listingsData = listingsData.dropna(" ")

