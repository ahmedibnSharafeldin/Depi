#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a function that takes a name as input and prints a greeting message.

# Write a function that takes two numbers as input and returns their sum

# Write a function that takes three numbers as input and returns the maximum number.


# In[1]:


def greeting (name):
    print(f"Ahlaan ya {name}")
name_1 = "Ibrahim"
greeting(name_1)


# In[2]:


def summation(a,b):
    return a + b
x = 55
y = 21
summation(x,y)


# In[5]:


def give_max(a,b,c):
    collect= [a,b,c]
    return max(collect)
x = 55
y = 41
z = 1000
give_max(x,y,z)


# In[ ]:


# Write a function that takes a number as input and returns whether the number is even or odd.

# Write a function that takes a string as input and returns the number of vowels in the string.


# In[8]:


def ev_od (num):
    if num%2 ==0 :
        return print(f" {num} is even")
    else:
        return print(f" {num} is odd")
num = 99 
ev_od(num)
num_s = 50
ev_od(num_s)


# In[15]:


def vowels_sum (string:str):
    collect = 0
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string.lower():
        if letter  in vowels:
            collect +=1
 
    return collect
my_string = "Ahla...HellO"
vowels_sum(my_string)
            


# In[ ]:


# Write a program to select a specific column


# In[ ]:


#Write a program to read a CSV file into a DataFrame and print the first 5 rows.

# Write a program to select a specific column


# In[ ]:





# In[24]:


import pandas as pd
df = pd.read_csv(r"C:\Users\Dell\Desktop\Data_Camp_files\Exploratory Data Analysis in SQL\ev311.csv")
df.head(5)


# In[22]:


df['street'].head()


# In[ ]:


# Write a program to filter rows where the 'Quantity' column is greater than 3.

# Write a program to sort the DataFrame by the 'Quantity' column in descending order.


# In[23]:


df.sort_values(by='id', ascending=False)


# In[27]:


# set a coulmn as an index in the dataframe
df.set_index('id', inplace = True)
df.head()
# Remove duplicates 

# Drop a column


# In[28]:


df["street"].drop_duplicates()


# In[29]:


df.head()


# In[33]:


df.drop(['description'], axis = 1, inplace = True)
df.head()


# In[ ]:




