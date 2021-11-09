#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


def get_db_url(db_name):
    from env import user, host, password
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'


# In[36]:


def new_titanic_data():
    sql = """
    SELECT * FROM passengers;
    """
    df = pd.read_sql(sql, get_db_url('titanic_db'))


# In[37]:


def get_titanic_data():
    
    if os.path.isfile('titanic.csv'):
        return pd.read_csv('titanic.csv')
    else:
        # read the SQL query into a dataframe
        df = new_titanic_data()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv('titanic.csv')

        # Return the dataframe to the calling code
        return df  


# In[38]:


get_titanic_data()


# In[39]:


def new_iris_data():
    sql = """
    SELECT species_id, species_name, sepal_length, sepal_width, petal_length, petal_width
    FROM measurements
    JOIN species USING(species_id);
    """
    df = pd.read_sql(sql, get_db_url('iris_db'))


# In[40]:


def get_iris_data():
    
    if os.path.isfile('iris.csv'):
        return pd.read_csv('iris.csv', index_col = 0)
    else:
        # read the SQL query into a dataframe
        df = new_iris_data()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv('iris.csv')

        # Return the dataframe to the calling code
        return df  


# In[41]:


get_iris_data()


# In[46]:


def new_telco_data():
    sql = """
    SELECT *
    FROM customers
    JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id
    JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
    JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id;
    """
    df = pd.read_sql(sql, get_db_url('telco_churn'))


# In[47]:


def get_telco_data():
    
    if os.path.isfile('telco.csv'):
        return pd.read_csv('telco.csv', index_col = 0)
    else:
        # read the SQL query into a dataframe
        df = new_telco_data()
        
        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv('telco.csv')

        # Return the dataframe to the calling code
        return df  


# In[48]:


get_telco_data()


# In[45]:





# In[ ]:




