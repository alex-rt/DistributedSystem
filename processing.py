#!/usr/bin/env python
# coding: utf-8

# In[1]:



#MASSIVE DATA MANAGEMENT 
#PARCIAL 2
#ALEJANDRO RODRIGUEZ TRILLO
#ANDRESS ARANA BEJAR


import pymongo
import numpy as np
import pandas as pd


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Parcial1"]
mycol = mydb["alejandro_rodriguez_covid"]



# In[2]:


result = mycol.aggregate([

    { "$match": {"CLASIFICACION_FINAL": "3" }},
    { "$group": {
        "_id": 
            "$ENTIDAD_RES"
        ,
        "count": { "$sum": 1 }
    }}
])


# In[3]:


datos = (list(result))
df = pd.DataFrame(datos)
df = df.apply(pd.to_numeric)


# In[4]:


newdf = df.sort_values(by= "_id")
newnew = newdf.reset_index(drop=True)


# In[5]:


newnew


# In[6]:


estados = [["Aguascalientes"],
["Baja California"],
["Baja California Sur"],
["Campeche"],
["Coahuila de Zaragoza"],
["Colima"],
["Chiapas"],
["Chihuahua"],
["Ciudad de México"],
["Durango"],
["Guanajuato"],
["Guerrero"],
["Hidalgo"],
["Jalisco"],
["Estado de México"],
["Michoacán de Ocampo"],
["Morelos"],
["Nayarit"],
["Nuevo León"],
["Oaxaca"],
["Puebla"],
["Querétaro"],
["Quintana Roo"],
["San Luis Potosí"],
["Sinaloa"],
["Sonora"],
["Tabasco"],
["Tamaulipas"],
["Tlaxcala"],
["Veracruz de Ignacio de la Llave"],
["Yucatán"],
["Zacatecas"]]


# In[9]:


df_new = pd.concat([newnew, pd.DataFrame(estados)], axis=1)
df_new.columns = ["ID", "CASOS CONFIRMADOS", "ESTADO"]
df_new = df_new[["ID", "ESTADO", "CASOS CONFIRMADOS"]]


# In[10]:


df_new


# In[21]:


result2 = mycol.aggregate([

    { "$match": { "$and": [ {"CLASIFICACION_FINAL": "3" }, { "FECHA_DEF": { "$ne": '9999-99-99'}} ]}},
    { "$group": {
        "_id": 
            "$ENTIDAD_RES"
        ,
        "count": { "$sum": 1 }
    }}
])


# In[22]:


datos2 = (list(result2))
df2 = pd.DataFrame(datos2)
df2 = df2.apply(pd.to_numeric)


# In[23]:


newdf2 = df2.sort_values(by= "_id")
newnew2 = newdf2.reset_index(drop=True)


# In[24]:


newnew2


# In[25]:


newnew2.columns = ["ID", "FALLECIMIENTOS"]
del newnew2["ID"]


# In[26]:


newnew2


# In[27]:


resultado = pd.concat([df_new, newnew2], axis=1)


# In[28]:


resultado.columns = ["ID", "ESTADO", "CASOS CONFIRMADOS", "FALLECIMIENTOS"]


# In[29]:


resultado


# In[36]:


resultado.to_csv('output_covid.csv', encoding='utf-8')


# In[ ]:




