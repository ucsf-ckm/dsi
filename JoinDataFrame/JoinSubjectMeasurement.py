
# coding: utf-8

# In[19]:


import pandas as pd

from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())


# In[20]:


subjects = pd.read_csv("subject.csv")


# In[21]:


print(subjects)


# In[22]:


measurements = pd.read_csv("measurement.csv")


# In[23]:


print(measurements)


# In[31]:


combined_df = pysqldf("SELECT * FROM subjects JOIN measurements     ON subjects.subject_id = measurements.subject_id     WHERE gender = 'M' AND data > 105")


# In[32]:


print(combined_df)

