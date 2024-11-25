#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = {
    'Employee': ['John Doe1', 'Anna2 Smith', 'Peter 3Jones', 'Lucy Brown4', 'Eve Clark5',
                 'Tom Wilson6', 'Grace7 Lee', 'Sam 8Green', 'Emma White9', 'James Black10',
                 'John Doe1', 'Anna2 Smith', None, 'Lucy Brown4', 'Eve Clark5',
                 'Tom Wilson6', 'Grace7 Lee', 'Sam 8Green', None, 'James Black10',
                 'Alice White11', 'Bob Davis12', 'Clara13 Adams', 'David14 Evans', 'Oscar King15'],
    'Salary': [55000, 60000, None, 45000, 48000,
               70000, 52000, None, 51000, 57000,
               55000, 60000, None, 45000, 48000,
               70000, None, 75000, 51000, None,
               49000, 62000, 53000, None, 58000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Sales',
                   'IT', 'HR', None, 'Finance', 'Sales',
                   'IT', 'HR', None, 'IT', 'Sales',
                   'IT', 'HR', None, 'Finance', 'Sales',
                   'Marketing', 'HR', 'Finance', 'IT', 'Marketing'],
    'City': ['New York', 'Los Angeles', 'Chicago',
             'Houston', 'Phoenix', 'San Francisco',
             'Dallas', None, 'Austin', 'Seattle',
             'New York', 'Los Angeles', None, 'Houston', 'Phoenix',
             'San Francisco', 'Dallas', None, 'Austin', 'Seattle',
             'Boston', 'Miami', 'Atlanta', 'Denver', 'Orlando'],
    'Phone_Number': ['+1-202-555-0171', '+44-20-7946-0958', '+1-202-555-0143', '+49-30-1234567', '+91-98765-43210',
                     '+1-202-555-0187', '+44-20-7946-0675', '+1-202-555-0199', '+49-30-9876543', '+91-98765-12345',
                     '+1-202-555-0171', '+44-20-7946-0958', None, '+49-30-1234567', '+91-98765-43210',
                     '+1-202-555-0187', '+44-20-7946-0675', None, '+49-30-9876543', None,
                     '+1-202-555-0165', '+44-20-7946-0345', '+1-202-555-0137', '+49-30-1357246', '+91-98765-56789'],
    'Hire_Date': ['2015-03-01', '2017-07-15', '2018-01-20', '2016-11-05', '2020-06-30',
                  '2014-04-17', '2019-10-11', '2021-09-25', '2016-02-13', '2015-05-08',
                  '2015-03-01', '2017-07-15', '2018-01-20', '2016-11-05', '2020-06-30',
                  '2014-04-17', '2019-10-11', '2021-09-25', '2016-02-13', '2015-05-08',
                  '2017-08-20', '2018-11-22', '2019-01-30', '2020-03-17', '2021-05-29'],
    'Age': [28, 34, 45, 29, 30, 31, 33, 39, 37, 50, 
            28, 34, None, 29, 30, 31, 33, 39, None, 50, 
            24, 43, 32, 40, 29]
}


# In[2]:


import pandas as pd
df = pd.DataFrame(data)
df.head(5)
df.info()


# In[3]:


#Fill missing values fill 5 columns with different ways 
df['Salary'].fillna(0, inplace = True)
df['Age'].fillna(0, inplace = True)
df['Department'].fillna("Not_known", inplace = True)
df['Employee'].fillna("Not_known", inplace = True)
df['City'].fillna("Not_known", inplace = True)
df['Phone_Number'].fillna("++++", inplace = True)
df.head(5)


# In[2]:


# Clean the 'Employee' column (title case, remove non-alphabetical characters including digits)
df['Employee'] = df['Employee'].str.title()
df['Employee'] = df['Employee'].str.replace(r'[^a-zA-Z\s]', ' ', regex=True) 
df


# In[5]:


# Convert Salary column to float and round to the nearest thousand
df['Salary'] = df['Salary'].astype(float).round(-3)
df.head(5)


# In[9]:


# Add a new column "Full Name" and split it into "First Name" and "Last Name"
# Add a new column "Full Name" from the "Employee" column
df['Full Name'] = df['Employee']

# Split "Full Name" into "First Name" and "Last Name"
df[['First Name', 'Last Name']] = df['Full Name'].str.split(' ', expand=True, n = 1)

# Handle the case where the employee name is "Not Known"
df.loc[df['Employee'] == 'Not Known', ['Full Name', 'First Name', 'Last Name']] = 'Not Known'
df.head(15) 


# In[11]:


# Calculate the average salary
average_salary = df['Salary'].mean()

# Create the 'Salary_Above_Average' column
df['Salary_Above_Average'] = df['Salary'] > average_salary
df.head(5)


# In[12]:


# Split the 'Phone_Number' column into 'Country_Code' and 'Local_Number'
df[['Country_Code', 'Local_Number']] = df['Phone_Number'].str.split('-', n=1, expand=True)
df.head(5)


# In[13]:


# Further split 'Local_Number' into 'Area_Code' and 'Actual_Number'
df[['Area_Code', 'Actual_Number']] = df['Local_Number'].str.split('-', n=1, expand=True)
df.head(5)


# In[14]:


# Add a column for the length of the phone number
df['Phone_Number_Length'] = df['Phone_Number'].str.len()
df.head(5)


# In[17]:


df['Salary'].describe()


# In[18]:


# Add a new column to categorize salary into low, medium, high
# Define the bins and labels
bins = [0, 45000, 51000, float('inf')]
labels = ['Low', 'Medium', 'High']

# Create the 'Salary_Category' column
df['Salary_Category'] = pd.cut(df['Salary'], bins=bins, labels=labels)
df


# In[19]:


# Convert 'Hire_Date' to datetime
df['Hire_Date'] = pd.to_datetime(df['Hire_Date'])

# Extract year and month
df['Hire_Year'] = df['Hire_Date'].dt.year
df['Hire_Month'] = df['Hire_Date'].dt.month
df.head(5)


# In[21]:


from datetime import datetime
# Calculate 'Years_at_Company'
current_date = datetime.now()
df['Years_at_Company'] = (current_date - df['Hire_Date']).dt.days // 365
df.head(5)


# In[22]:


# Plot Scatter Plot of Salary vs Age
df.plot.scatter(x='Age', y='Salary', title='Scatter Plot: Salary vs Age')


# In[23]:


# Plot Barplot of Salary by Department
df.groupby('Department')['Salary'].mean().plot(kind='bar', title='Average Salary by Department') 


# In[24]:


# Plot Salary Distribution
df['Salary'].plot(kind='hist', bins=10, edgecolor='black', title='Salary Distribution') 


# In[25]:


# Filter out zero values
df_non_zero = df[df['Salary'] > 0]

# Plot Salary Distribution without zero values
df_non_zero['Salary'].plot(kind='hist', bins=10, edgecolor='black', title='Salary Distribution') 


# In[ ]:




